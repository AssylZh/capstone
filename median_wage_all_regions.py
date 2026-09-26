# Median wage by region — Republic of Kazakhstan, 2019–2025 (total, tenge)
import matplotlib.pyplot as plt
import numpy as np

years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]

data = {
    "Republic of Kazakhstan": [112281, 142718, 165816, 204149, 251356, 285677, 317512],
    "Astana city":            [165645, 198482, 216724, 258535, 297332, 327598, 386678],
    "Almaty city":            [142334, 170874, 189122, 231958, 283280, 325649, 377899],
    "Shymkent city":          [92274, 130685, 153883, 175588, 215906, 248579, 273905],
    "Abay":                   [None, None, None, None, 218693, 247355, 289910],
    "Akmola":                 [99224, 124919, 145890, 182318, 230999, 259430, 297468],
    "Aktobe":                 [110525, 142495, 154081, 199503, 252334, 284898, 308920],
    "Almaty":                 [96224, 124578, 156300, 178077, 213464, 270266, 294517],
    "Atyrau":                 [159911, 195936, 228244, 269234, 322365, 338890, 367936],
    "Batys Kazakhstan":       [96944, 125081, 149121, 184607, 222094, 252861, 272988],
    "Zhambyl":                [94472, 114922, 140006, 176842, 212624, 242728, 281690],
    "Zhetisu":                [None, None, None, None, 196693, 233593, 265753],
    "Karagandy":              [116536, 145858, 166643, 213507, 269939, 306004, 332680],
    "Kostanay":               [104861, 130612, 145003, 189033, 232048, 260936, 299870],
    "Kyzylorda":              [97281, 126696, 146665, 184458, 233236, 259472, 295704],
    "Mangystau":              [148063, 176112, 192123, 257658, 323778, 350314, 374050],
    "Pavlodar":               [119567, 145230, 173067, 207543, 261708, 306438, 341607],
    "Soltustik Kazakhstan":   [94482, 119484, 131662, 171387, 187125, 231234, 251107],
    "Turkistan":              [90107, 119823, 145819, 177900, 222054, 242328, 261028],
    "Ulytau":                 [None, None, None, None, 392283, 404105, 457339],
    "Shygys Kazakhstan":      [106412, 133059, 162649, 188634, 251799, 292448, 316601],
}

# Distinct color palette (one per region), national total gets a bold neutral color
palette = [
    "#e8b04b", "#4f8fdb", "#e0607e", "#5bc1a8", "#c77dff", "#f2994a",
    "#61a0af", "#d64550", "#8ac926", "#b088f9", "#4dd0e1", "#ffb703",
    "#f77f00", "#7986cb", "#43aa8b", "#f94144", "#90be6d", "#577590",
    "#f3722c", "#277da1", "#9b5de5",
]

fig, ax = plt.subplots(figsize=(13, 7))

for i, (region, values) in enumerate(data.items()):
    y = np.array(values, dtype=float)  # None -> nan, so gaps break the line naturally
    is_national = region == "Republic of Kazakhstan"
    ax.plot(
        years, y,
        marker="o",
        markersize=4,
        linewidth=3 if is_national else 1.8,
        linestyle="--" if is_national else "-",
        color="#333333" if is_national else palette[i % len(palette)],
        label=region,
    )

ax.set_title("Median Wage of Employees by Region — Republic of Kazakhstan (2019–2025)", fontsize=14, weight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Median wage (tenge)")
ax.yaxis.set_major_formatter(lambda v, pos: f"{int(v/1000)}k")
ax.grid(True, alpha=0.25)
ax.set_xticks(years)

# Legend outside the plot so 21 regions stay readable
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8, frameon=False)

plt.tight_layout()
plt.show()