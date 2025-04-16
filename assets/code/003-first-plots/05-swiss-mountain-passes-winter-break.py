import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("paesse.csv", sep=";")
df["passhöhe"] = pd.to_numeric(df["passhöhe"], errors="coerce")

# Define elevation category
def elevation_category(m):
    if pd.isna(m):
        return "Unknown"
    elif m <= 1500:
        return "1000–1500 m"
    elif m <= 2000:
        return "1500–2000 m"
    else:
        return "above 2000 m"

df["elevation_category"] = df["passhöhe"].apply(elevation_category)

# Filter: only passes with winter closure
df_sperre = df[df["wintersperre"] == "Ja"].copy().reset_index(drop=True)

# Define custom month order (centered around winter)
reordered_months = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
month_labels = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
month_map = {mo: i + 1 for i, mo in enumerate(reordered_months)}

# Color palette by elevation category
palette = {
    "1000–1500 m": sns.color_palette("viridis", 3)[2],
    "1500–2000 m": sns.color_palette("viridis", 3)[1],
    "above 2000 m": sns.color_palette("viridis", 3)[0]
}

# Process closure periods
sperren_shifted = []
for i, row in df_sperre.iterrows():
    try:
        start = int(row["sperre_beginn"])
        ende = int(row["sperre_ende"])
        m_start = month_map.get(start)
        m_ende = month_map.get(ende)
        if m_start is None or m_ende is None:
            continue

        color = palette.get(row["elevation_category"], "#CCCCCC")
        elevation = row["passhöhe"]

        if m_ende >= m_start:
            sperren_shifted.append((i, m_start, m_ende - m_start + 1, color, elevation))
        else:
            sperren_shifted.append((i, m_start, 12 - m_start + 1, color, elevation))
            sperren_shifted.append((i, 1, m_ende, color, elevation))
    except Exception:
        continue

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

for y, start, duration, color, _ in sperren_shifted:
    ax.broken_barh([(start, duration)], (y - 0.4, 0.8), facecolor=color, alpha=0.9)

ax.set_yticks(range(len(df_sperre)))
ax.set_yticklabels(df_sperre["name"])

# Secondary y-axis showing elevations
ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim())
ax2.set_yticks(range(len(df_sperre)))
ax2.set_yticklabels([f"{int(h)} m" for h in df_sperre["passhöhe"][::-1]])
ax2.set_ylabel("Pass elevation", rotation=270, labelpad=30)

# X-axis and labels
ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_labels)
ax.set_xlabel("Months (winter-centered)", labelpad=20)
ax.set_title("Winter Closures of Swiss Mountain Passes – colored by elevation", pad=20)
ax.invert_yaxis()
ax.grid(True, axis="x", linestyle="--", color="#CCCCCC")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=label) for label, color in palette.items()]
ax.legend(handles=legend_elements, title="Elevation category", loc="lower right")

plt.subplots_adjust(left=0.2, right=0.88, top=0.92, bottom=0.08)
plt.show()
