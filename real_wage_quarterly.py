"""
quarterly real wage trend for my regions of interest
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

SHEET_ID = "1Uud8SmvilgxCUmgJ5Uezgj9ES9HyMbwtBsfx2Xpca1I"
EXCEL_PATH = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=xlsx"
SHEET_NAME = "Quarterly_Panel"

# picked these 4 because they tell the clearest story - two oil regions
# (Atyrau, Mangystau) vs the capital and Almaty region
REGIONS = ["Atyrau", "Mangystau", "Astana city", "Almaty"]
COLORS = {"Atyrau": "#e34948", "Mangystau": "#eda100", "Astana city": "#2a78d6", "Almaty": "#1baf7a"}

# ---------------------------------------------------------------------------
# load the data
# ---------------------------------------------------------------------------
df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

# real_wage_mean is a formula column in the sheet, but if it comes back empty
# (happens if excel wasn't recalculated before saving) just compute it here
if "real_wage_mean" not in df.columns or df["real_wage_mean"].isna().all():
    df["real_wage_mean"] = df["wage_mean"] / (df["cpi_index"] / 100)

# year+quarter as one label so it's easier to plot on the x-axis
df["period"] = df["year"].astype(str) + "Q" + df["quarter"].astype(str)

pivot = df.pivot(index="period", columns="region", values="real_wage_mean")

# columns come out unsorted so fix the order manually (year, then quarter)
periods = sorted(pivot.index, key=lambda p: tuple(int(x) for x in p.split("Q")))
pivot = pivot.reindex(periods)

# only keep quarters where ALL 4 regions have a value - otherwise the lines
# get gaps and look broken
subset = pivot[REGIONS].dropna()
print(f"got {len(subset)} full quarters out of {len(pivot)} total")
print(subset.round(0))

# ---------------------------------------------------------------------------
# plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5))

for region in REGIONS:
    ax.plot(subset.index, subset[region], marker="o", markersize=4,
             linewidth=2, color=COLORS[region], label=region)

ax.set_ylabel("Real wage, Dec 2020 tenge")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v/1000:.0f}k"))  # show as "450k" not "450000"
ax.grid(axis="y", color="#e1e0d9", linewidth=0.8)
ax.set_axisbelow(True)

# don't need the top/right box lines, looks cleaner without them
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
plt.xticks(rotation=45, ha="right")

ax.legend(loc="upper left", frameon=False, fontsize=9, ncol=4)
plt.title("Quarterly real wage by region, Kazakhstan (Q1 2023 - Q2 2026)",
          fontsize=13, fontweight="bold", loc="left")
plt.tight_layout()
plt.savefig("quarterly_real_wage_trend.png", dpi=150)
print("saved quarterly_real_wage_trend.png")