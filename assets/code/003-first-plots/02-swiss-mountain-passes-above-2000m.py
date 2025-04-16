import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("paesse.csv", sep=";")

# Filter: only passes above 2000 meters
df_above_2000 = df[df["passhöhe"] > 2000].sort_values(by="passhöhe", ascending=False)

# Plot style
sns.set_theme(style="ticks")
fig, ax = plt.subplots(figsize=(10, 10))

# Gradient color across bars (not within each bar)
rocket_palette = sns.color_palette("rocket", n_colors=len(df_above_2000))

barplot = sns.barplot(
    data=df_above_2000,
    x="passhöhe",
    y="name",
    hue="name",  # each bar gets its own color
    dodge=False,  # important when using hue + barplot
    palette=rocket_palette,
    ax=ax,
    width=0.6,
    legend=False  # don't show a color legend
)

# Add labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f m", label_type="edge", padding=3)

# Labels and title
ax.set_xlabel("Pass Elevation (meters)", labelpad=10)
ax.set_ylabel("Pass Name", labelpad=15)
ax.set_title("Swiss Mountain Passes Above 2000 m", pad=20)

# Spines (borders)
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_color("#181818")
    ax.spines[spine].set_linewidth(1)

# Gridlines (only on x-axis, for orientation)
ax.grid(True, axis="x", linestyle="--", linewidth=0.5, color="#CCCCCC")
ax.grid(False, axis="y")

# Add extra space on the right
xmax = df_above_2000["passhöhe"].max()
ax.set_xlim(0, xmax + 300)

plt.tight_layout()
plt.show()
