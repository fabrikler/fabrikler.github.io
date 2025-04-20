---
date: '2025-04-15T07:11:51+02:00'
draft: false
title: 'My favourite animals are pandas (not the lazy bears) — 003'
background: "/img/001/mountain-passes-overview-005.jpg"
---

{{< caption src="/img/001/mountain-passes-overview-011.jpg" alt="Foggy Road at Gotthard Pass" text="From sun to thick fog – the weather can change in minutes" >}}

With my freshly scraped and cleaned CSV in hand, I started digging into <a href="https://pandas.pydata.org/" target="_blank" rel="noopener">Pandas</a>
, <a href="https://matplotlib.org/" target="_blank" rel="noopener">Matplotlib</a> and <a href="https://seaborn.pydata.org/" target="_blank" rel="noopener">Seaborn</a> to plot my first chart.

I decided to start with a classic overview by sorting the passes by elevation.

#### Important note

📌 _The highest points might differ slightly from the maximum elevations listed in other sources. In most cases, the passes are shown a few meters higher elsewhere. I based my measurements on GPX data, which always refers to the highest point on the road itself, not to parking areas or viewing platforms._

### Overview over the dataset

{{< caption src="/img/003/01-swiss-mountain-passes-by-elevation.png" alt="Swiss Mountain Pass Data by Elevation" text="First Overview" >}}


<details>
  <summary>🔍 You can see the code of the overview here:</summary>  
{{< snippet "003-first-plots/01-swiss-mountain-passes-by-elevation.py" >}}
</details>
<br>


I also grouped them into three elevation categories:

**1000 to 1500 meters**  
These are entry-level passes, often found in lower mountain ranges like the Jura. They require less preparation, and even in bad weather it's usually easy to find shelter or descend quickly.

**1500 to 2000 meters**  
This is the transition zone between the entry-level and alpine passes. They can be tricky due to temperature fluctuations, and it can get cold very quickly, especially during descents.

**Above 2000 meters**  
This is true alpine terrain and shouldn't be taken lightly. These passes are often exposed, with steep switchbacks, and they require more preparation in terms of weather forecasts, proper clothing, and food.


---

### Top passes over 2000m

I also wanted to create a separate overview of the passes above 2000 meters.

{{< caption src="/img/003/02-swiss-mountain-passes-above-2000m.png" alt="Swiss Mountain Passes over 2000m" text="Top passes over 2000m" >}}

<details>
  <summary>🔍 You can see the code of the top passes here:</summary>  
{{< snippet "003-first-plots/02-swiss-mountain-passes-above-2000m.py" >}}
</details>
<br>

---

### How does the overall elevation correlate with the length of the route?

I found that routes leading to higher mountain passes tend to be slightly longer overall. In many cases, the approach from civilization takes more time. A clear outlier: the Great St. Bernhard Pass, with nearly 80 km of route length.

{{< caption src="/img/003/03-swiss-mountain-passes-elevation-distance.png" alt="Swiss Mountain Passes Elevation to Distance Data" text="Elevation x Distance" >}}

<details>
  <summary>🔍 You can see the code of the top passes here:</summary>  
{{< snippet "003-first-plots/03-swiss-mountain-passes-elevation-distance.py" >}}
</details>
<br>

---

### Which one is the steepest?

Everything above 15% is steep. But if a track hits 20% or more, you’ll probably have to push. Weissenstein and Col des Montets both have some serious segments.

{{< caption src="/img/003/04-swiss-mountain-passes-max-gradient.png" alt="Swiss Mountain Passes by max Gradient" text="Looking for Kneebreakers" >}}

<details>
  <summary>🔍 You can get a glimpse of the steepness here:</summary>  
{{< snippet "003-first-plots/04-swiss-mountain-passes-max-gradient.py" >}}
</details>
<br>

---

### Winter Closures

Many passes close during winter. I wanted to find out when they close and for how long.

{{< caption src="/img/003/05-swiss-mountain-passes-winter-break.png" alt="Swiss Mountain Passes by Winter Closures" text="Closing times for riders" >}}

<details>
  <summary>🔍 You'll find the code to this plot here:</summary>  
{{< snippet "003-first-plots/05-swiss-mountain-passes-winter-break.py" >}}
</details>
<br>

---

👉 This small project provided a great first dive into Pandas, Matplotlib and Seaborn. Along the way, a few interesting insights emerged. It would be exciting to take things further by mapping the data, exploring it in 3D or building something interactive.

For now, it was satisfying to gain a clear sense of the key characteristics of the passes, such as elevation, distance, gradient and seasonality, and to lay the foundation for future ideas.
