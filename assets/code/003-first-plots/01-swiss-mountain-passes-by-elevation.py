import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("paesse.csv", sep=";")

# Define elevation category
def elevation_category(m):
    if m <= 1500:
        return "1000-1500 m"
    elif m <= 2000:
        return "1500-2000 m"
    else:
        return "above 2000 m"

df["elevation_category"] = df["passhöhe"].apply(elevation_category)
df_sorted = df.sort_values(by="passhöhe", ascending=False)

# Set visual theme
sns.set_theme(style="ticks")  # kein Grid von Seaborn automatisch

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

barplot = sns.barplot(
    x="passhöhe",
    y="name",
    data=df_sorted,
    hue="elevation_category",
    dodge=False,
    palette="viridis",
    ax=ax
)

# Add labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f m", label_type="edge", padding=3)

# Labels and layout
ax.set_xlabel("Pass Elevation (meters)", labelpad=10)
ax.set_ylabel("Pass Name", labelpad=15)
ax.set_title("Swiss Mountain Passes by Elevation", pad=20)
ax.legend(title="Elevation Category", loc="lower right")

# Spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#181818")
ax.spines["left"].set_linewidth(1)
ax.spines["bottom"].set_color("#181818")
ax.spines["bottom"].set_linewidth(1)

# Vertical "height lines"
ax.grid(True, axis="x", linestyle="--", linewidth=0.5, color="#CCCCCC")
ax.grid(False, axis="y")

# Spacing
plt.subplots_adjust(left=0.25, right=0.95, top=0.9, bottom=0.1)
plt.tight_layout()
plt.show()
