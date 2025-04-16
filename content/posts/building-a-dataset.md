---
date: '2025-04-10T07:11:51+02:00'
draft: false
title: 'Building a Dataset — 002'
background: "/img/001/mountain-passes-overview-009.jpg"
---
{{< caption src="/img/001/mountain-passes-overview-009.jpg" alt="Festka Bike riding in the Alps" text="Festka Frameset with Obermayer Wheels at Gotthard Tremola" >}}

If you ride mountain passes long enough, the question is no longer _if_ you’ll ride again, but _which one_. And that’s exactly where the problem begins.

Performance isn’t everything in cycling.

Climbing - as we call it - has something mystical to it. Almost ritualistic.

Up in the mountains, while your breathing gets heavier and your cadence slower, you can slip into altered states. Some say it’s just oxygen deprivation. But hey, the high is kind of nice.

The mountains are also a bit like forests:

In Japan, they have a concept for this: <strong><a href="https://en.wikipedia.org/wiki/Shinrin-yoku" target="_blank" rel="noopener">Shinrin Yoku</a></strong>, or <em>forest bathing</em>.

It’s the art of immersing yourself in nature with all senses. Not as a workout, but as therapy.  

That’s exactly what climbing does. **Cycling is a tool of awareness.**

But before we talk about epic climbs and becoming some sort of monk,  
let’s start with the most basic question:

What exactly is a pass?


{{< caption src="/img/001/mountain-passes-overview-010.jpg" alt="Serpentines at Gotthard Tremola" text="Cobble Serpentines at Gotthard" >}}



### The messy truth behind beautiful roads

Most cyclists have a gut feeling for what counts as a real pass.
But try to define it, and things get a bit fuzzy:

- Is it about the altitude?
- The number of switchbacks?
- Does it have to cross a canton? A border?
- Do we need to see some snow, even in summer?
- And does it still count if the top isn’t really a "peak", but more like a soggy meadow with a bus stop?

Turns out: There _are_ definitions. But they’re blurry.

The one I chose (for this project at least) goes something like this:

_A **pass road** is a rideable route that crosses a mountain ridge at its lowest practical point and connects two valleys._

In other words: It’s not about how _high_ you climb, but _where_ you cross.

And there’s a deeper explanation behind it.

{{< caption src="/img/001/mountain-passes-overview-005.jpg" alt="Source of the young Rhone River near Rhone Glacier" text="The young Rhone, fresh from its source" >}}

When you cross a pass, you don’t just change valleys. You also cross watersheds, language regions, cultural peculiarities, and micro-climates. And sometimes, the cheese tastes completely different.

So crossing a pass has something of an initiation rite with the topology you’re moving through. What defines a pass is less about altitude, and more about **function** and transformation.

Let's define: The label _“Pass”_ isn’t tied to a specific height.  
It’s not about numbers. It’s about **crossing**, **connection**, **terrain** – and cultural as well as mental expansion.

So with that in mind, I began digging.

### Scraping for clarity

I quickly found a cohesive and regularly updated list provided by the Swiss Touring Club (TCS) -
 a solid collection of <strong><a href="https://www.tcs.ch/de/tools/verkehrsinfo-verkehrslage/paesse-in-der-schweiz.php" target="_blank" rel="noopener">77 key mountain passes</a></strong></em>.

To extract the data, I wrote a custom scraper using Python and <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank" rel="noopener">BeautifulSoup</a>.

It crawled through the page structure and pulled in names, altitudes, routes, distances, and metadata like gradient, winter status, and whether there’s a restaurant or an EV charging station at the top.

I won’t publish the full scraper here, but the idea is simple:

- Open the saved HTML file
- Loop through each pass block
- Parse and clean the relevant fields
- Export everything to a CSV file for further analysis

That's it.

{{< caption src="/img/002/paesse-first-csv-overview-002.png" alt="csv snippet of swiss mountain peaks" text="building the dataset" >}}


### Cleaning and arranging

_(Insert image of the cleaned table here)_

The raw list was almost perfect, but still needed a bit of cleaning.

I used Excel formulas like `=TRIM(CLEAN(B2))` to get rid of weird spacing or invisible characters. Some fields were merged and had to be split using Power Query.

I also had to standardize all numerical values:

Distances, gradients, and altitudes were converted into float format, because Python treats numbers differently based on their type.


{{% prologue class="prologue-box prologue-box--transparent" %}}
A **string** is just a piece of text. Even if it _looks_ like a number.  
For example, `"8,5"` (with a comma) is not a valid number in Python, it's treated as a string because of the **comma instead of a dot**, which Python doesn’t recognize as a decimal separator.

So while `"8,5"` might mean _eight point five_ to a human, to Python it's just a text label, like `"apple"` or `"hello"`.

To use it in calculations, it first has to be cleaned and converted into a proper number format, like `8.5`.
{{% /prologue %}}

So before I could analyze anything, I had to replace commas with dots (`8,5` → `8.5`) and drop anything that couldn't be converted cleanly.

It’s a small step. But without it, you’re basically comparing apples and strings.
And funny enough, this was one of the first things I learned when starting with Python.

After cleaning and exporting the data, I loaded it into a simple table and started checking for outliers. One or two passes had gradients over 25% – which didn’t feel right. Some had distances of "99 km" that were clearly a typo. Where necessary, I fixed them manually.

{{< caption src="/img/002/komoot-overview-001.png" alt="csv snippet of swiss mountain peaks" text="building the dataset" >}}

### From table (csv) to terrain (gpx)

Once the cleaned CSV was ready, I moved on to the next step:  
**building every route manually in Komoot.**

I’ve built hundreds of GPS tracks over the years, and I pay a lot of attention to clean route design.

My routes always take multiple parameters into consideration.  

Especially when planning off-road (which wasn’t the case here), I usually incorporate practical tweaks, like avoiding traffic-heavy roads, passing through supermarkets or gas stations to refill calories, and choosing more scenic alternatives when available.

So with that background, I followed a few simple rules for the mountain pass set:

- First, I hand-picked **50 out of the 77 passes** provided in the dataset. Mostly the highest and most iconic ones.

- If a route went through long tunnels or busy highways, I picked the alternative - usually a quieter, paved road. Because beauty and safety matter.

- If there was a classic segment - like the old north ramp at Gotthard, a historic cobbled postal road - I chose that for full authenticity. 

- I tried to connect the routes **from train station to train station**, or **church to church**, or **bridge to bridge** - to give them a sense of cohesion. A kind of narrative logic.

It took a while. 😅
But in the end, every route had a soul.

{{< caption src="/img/001/mountain-passes-overview-004.jpg" alt="Cyclist Vitor climbing the northern ramp of Gotthard Pass" text="Vitor pushing watts on the northern ramp of Gotthard Pass" >}}


### Building a GPX-Stats-Extractor

While the original TCS data gave a good overview to start building in Komoot,  
the dataset had to be updated with the **real distance** and the **actual elevation gain**.

Therefore, I built a Jupyter Notebook called “GPX Stats Extractor.”

<details>
  <summary>Loading Libraries:</summary>  
{{< snippet "gpx-extractor/001-gpx-extractor.py" >}}
</details>
<br>

<details>
  <summary>Analyze a single GPX file and extract elevation, distance & gradients:</summary>  
{{< snippet "gpx-extractor/002-gpx-extractor.py" >}}
</details>
<br>

<details>
  <summary>Analyze all GPX files in a folder and export results to CSV:</summary>  
{{< snippet "gpx-extractor/003-gpx-extractor.py" >}}
</details>
<br>

<details>
  <summary>Trigger the analysis with the local GPX folder path:</summary>  
{{< snippet "gpx-extractor/004-gpx-extractor.py" >}}
</details>
<br>


Once those values were extracted from the GPX files, the table was ready for visualization.

👉 [Download CSV file](/downloads/2504_paesse.csv)


{{< caption src="/img/001/mountain-passes-overview-007.jpg" alt="Cyclist at Gotthardpass" text="Thorben climbing through the north ramp at Gotthard" >}}


In the next post, I’ll take you through the first visualizations –  
and show what data can reveal when you look at mountains not just with legs, but with code.