import matplotlib.pyplot as plt
import numpy as np

years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]

national = [112281, 142718, 165816, 204149, 251356, 285677, 317512]

zones = {
    "North": {
        "color": "#4f8fdb",
        "regions": {
            "Astana city":          [165645, 198482, 216724, 258535, 297332, 327598, 386678],
            "Akmola":               [99224, 124919, 145890, 182318, 230999, 259430, 297468],
            "Kostanay":             [104861, 130612, 145003, 189033, 232048, 260936, 299870],
            "Soltustik Kazakhstan": [94482, 119484, 131662, 171387, 187125, 231234, 251107],
            "Pavlodar":             [119567, 145230, 173067, 207543, 261708, 306438, 341607],
        }
    },
    "South": {
        "color": "#e0607e",
        "regions": {
            "Almaty city":   [142334, 170874, 189122, 231958, 283280, 325649, 377899],
            "Shymkent city": [92274, 130685, 153883, 175588, 215906, 248579, 273905],
            "Almaty":        [96224, 124578, 156300, 178077, 213464, 270266, 294517],
            "Zhetisu":       [None, None, None, None, 196693, 233593, 265753],
            "Zhambyl":       [94472, 114922, 140006, 176842, 212624, 242728, 281690],
            "Turkistan":     [90107, 119823, 145819, 177900, 222054, 242328, 261028],
            "Kyzylorda":     [97281, 126696, 146665, 184458, 233236, 259472, 295704],
        }
    },
    "East": {
        "color": "#e8b04b",
        "regions": {
            "Shygys Kazakhstan": [106412, 133059, 162649, 188634, 251799, 292448, 316601],
            "Abay":              [None, None, None, None, 218693, 247355, 289910],
            "Karagandy":         [116536, 145858, 166643, 213507, 269939, 306004, 332680],
            "Ulytau":            [None, None, None, None, 392283, 404105, 457339],
        }
    },
    "West": {
        "color": "#5bc1a8",
        "regions": {
            "Aktobe":           [110525, 142495, 154081, 199503, 252334, 284898, 308920],
            "Atyrau":           [159911, 195936, 228244, 269234, 322365, 338890, 367936],
            "Batys Kazakhstan": [96944, 125081, 149121, 184607, 222094, 252861, 272988],
            "Mangystau":        [148063, 176112, 192123, 257658, 323778, 350314, 374050],
        }
    },
}

sub_palette = ["#e8b04b", "#4f8fdb", "#e0607e", "#5bc1a8", "#c77dff", "#f2994a", "#61a0af"]

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for ax, (zone_name, zone) in zip(axes, zones.items()):
    for i, (region, values) in enumerate(zone["regions"].items()):
        y = np.array(values, dtype=float)
        ax.plot(years, y, marker="o", markersize=4, linewidth=2,
                color=sub_palette[i % len(sub_palette)], label=region)

    # national reference line
    ax.plot(years, national, linestyle="--", linewidth=2, color="#555b61",
             label="Republic of Kazakhstan")

    ax.set_title(f"{zone_name} zone", fontsize=13, weight="bold", color=zone["color"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Median wage (tenge)")
    ax.yaxis.set_major_formatter(lambda v, pos: f"{int(v/1000)}k")
    ax.grid(True, alpha=0.25)
    ax.set_xticks(years)
    ax.legend(fontsize=8, frameon=False, loc="upper left")

fig.suptitle("Median Monthly Wage by Region — Republic of Kazakhstan (2019–2025)",
             fontsize=15, weight="bold", y=1.0)
plt.tight_layout()
plt.show()