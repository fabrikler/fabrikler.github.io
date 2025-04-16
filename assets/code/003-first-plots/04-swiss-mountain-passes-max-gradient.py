import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("paesse.csv", sep=";")

# Sort and select top 20 steepest passes
df_top20 = df.sort_values(by="max_steigung", ascending=False).head(20)

# Plot style
sns.set_theme(style="ticks")
fig, ax = plt.subplots(figsize=(10, 10))

# Gradient color across bars (not within each bar)
rocket_palette = sns.color_palette("rocket", n_colors=20)

barplot = sns.barplot(
    data=df_top20,
    x="max_steigung",
    y="name",
    hue="name",  
    dodge=False,
    palette=rocket_palette,
    ax=ax,
    width=0.6,
    legend=False  
)

# Add value labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%", label_type="edge", padding=3)

# Labels and title
ax.set_xlabel("Maximum Gradient (%)", labelpad=10)
ax.set_ylabel("Pass Name", labelpad=15)
ax.set_title("Top 20 Swiss Mountain Passes by Maximum Gradient", pad=20)

# Spines (borders)
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_color("#181818")
    ax.spines[spine].set_linewidth(1)

# Gridlines (only vertical, for orientation)
ax.grid(True, axis="x", linestyle="--", linewidth=0.5, color="#CCCCCC")
ax.grid(False, axis="y")

xmax = df_top20["max_steigung"].max()
ax.set_xlim(0, xmax + 2)

plt.tight_layout()
plt.show()
