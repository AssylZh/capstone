"""
real wage growth by region, 2023-2025
this is the main chart for my thesis - shows which regions actually got
poorer in real terms even though nominal wages went up everywhere
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

SHEET_ID = "1AH1H0TtUlFASOqrJt1ZPMEEr8AzRVEDzCjcTounP1Pk"
EXCEL_PATH = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"
SHEET_NAME = "Master_Panel"

# 2023 is as far back as I can go for this since CPI data doesn't exist
# before then - can't compute real wages without it
YEAR_START = 2023
YEAR_END = 2025
NATIONAL_LABEL = "Republic of Kazakhstan"

COLOR_POSITIVE = "#2a78d6"
COLOR_NEGATIVE = "#e34948"
COLOR_NATIONAL = "#898781"

df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

# real_wage_median is a formula column in the sheet already, but just in
# case it comes through blank (happens if the sheet wasn't recalculated),
# work it out here instead
if "real_wage_median" not in df.columns or df["real_wage_median"].isna().all():
    df["real_wage_median"] = df["wage_median"] / (df["cpi_index"] / 100)

pivot = df.pivot(index="region", columns="year", values="real_wage_median")

# only regions with real wage data in both the start and end year
valid = pivot[[YEAR_START, YEAR_END]].dropna().index
growth = ((pivot.loc[valid, YEAR_END] / pivot.loc[valid, YEAR_START] - 1) * 100).sort_values()

print(f"Regions included ({len(growth)} of {len(pivot)} total):")
print(growth.round(1))

# ---------------------------------------------------------------------------
# plot: horizontal bar chart, sorted so it's easy to see who's below zero
# ---------------------------------------------------------------------------
colors = [
    COLOR_NATIONAL if region == NATIONAL_LABEL else (COLOR_NEGATIVE if val < 0 else COLOR_POSITIVE)
    for region, val in growth.items()
]

fig, ax = plt.subplots(figsize=(9, 0.35 * len(growth) + 2))
bars = ax.barh(growth.index, growth.values, color=colors, height=0.6)

ax.axvline(0, color="#c3c2b7", linewidth=1)  # zero line so negative growth stands out
ax.set_xlabel(f"Real wage growth, {YEAR_START}-{YEAR_END} (%, CPI-adjusted)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{'+' if v >= 0 else ''}{v:.0f}%"))
ax.grid(axis="x", color="#e1e0d9", linewidth=0.8)
ax.set_axisbelow(True)

# cleaner without the box around the whole thing
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)

# put the actual number next to each bar instead of making people read the axis
for bar, val in zip(bars, growth.values):
    offset = 0.3 if val >= 0 else -0.3
    ha = "left" if val >= 0 else "right"
    ax.text(val + offset, bar.get_y() + bar.get_height() / 2, f"{'+' if val >= 0 else ''}{val:.1f}%",
            va="center", ha=ha, fontsize=9)

# quick legend so it's clear what the colors mean
legend_handles = [
    plt.Rectangle((0, 0), 1, 1, color=COLOR_POSITIVE, label="Positive real growth"),
    plt.Rectangle((0, 0), 1, 1, color=COLOR_NEGATIVE, label="Negative real growth"),
    plt.Rectangle((0, 0), 1, 1, color=COLOR_NATIONAL, label="National average"),
]
ax.legend(handles=legend_handles, loc="lower right", frameon=False, fontsize=9)

plt.title(f"Real wage growth by region, Kazakhstan ({YEAR_START}-{YEAR_END})",
          fontsize=13, fontweight="bold", loc="left")
plt.tight_layout()
plt.savefig("real_wage_growth_by_region.png", dpi=150)
print("\nsaved real_wage_growth_by_region.png")