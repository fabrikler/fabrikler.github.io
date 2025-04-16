import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("paesse.csv", sep=";")

# Elevation categories
def elevation_category(m):
    if m <= 1500:
        return "1000-1500 m"
    elif m <= 2000:
        return "1500-2000 m"
    else:
        return "above 2000 m"

df["elevation_category"] = df["passhöhe"].apply(elevation_category)

# Set theme
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))

# Scatterplot: Distance vs. Elevation
scatter = sns.scatterplot(
    data=df,
    x="distanz_km",
    y="passhöhe",
    hue="elevation_category",
    palette="viridis",
    s=100,
    edgecolor="black",
    alpha=0.8,
    ax=ax
)

# Labels & title
ax.set_title("Elevation vs. Distance of Swiss Mountain Passes", pad=20)
ax.set_xlabel("Distance (km)", labelpad=10)
ax.set_ylabel("Elevation (m)", labelpad=10)
ax.legend(title="Elevation Category", loc="upper left")

# Spines: all four sides visible & dark gray
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_color("#181818")
    ax.spines[spine].set_linewidth(1)

plt.tight_layout()
plt.show()
