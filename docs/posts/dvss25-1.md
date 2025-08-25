---
date: 2025-07-07
authors:
  - silvio
categories:
  - DVSS
---

# DVSS - Day 1

Day 1 _on the fly_ notes of [MaLGa's Data Visualization Summer School 2025](https://malga.unige.it/education/schools/dvss/).

<!-- more -->

## Scientific communication

- science != scientific literacy (content/research vs process/impact/methods)
- assess/know the scientific literacy level of the audience

### Giorgia Lupi

<figure>
    <img src="../../../../assets/dvss/c2a44b70-d1ed-4d9e-bcaf-4360bd560d1d.jpg" alt="Uploaded image" />
    <figcaption>https://www.informationisbeautifulawards.com/showcase/204-nobels-no-degrees</figcaption>
</figure>

- peculiar use of space: chart diagonal orientation vs text lexicographic order, to convey information (e.g. "this should be read" vs "this should be seen") and to grab attention
- sample chart as legend
- [Approximating the components of Lupi's Nobel, no degrees](https://ssp3nc3r.github.io/post/approximating-the-components-of-lupi-s-nobel-no-degrees/)

### Federica Fragapane

<figure>
    <img src="../../../../assets/dvss/320802c6-1634-48c5-9c8a-5b50ce54ec58.webp" alt="Uploaded image" />
    <figcaption>https://www.behance.net/gallery/70033395/The-Most-Violent-Cities/</figcaption>
</figure>

- lollipop chart with polar plot at each marker to convey both relative and absolute magnitude at the same time
- design choices to empathize with data meaning (e.g. encode murder victims as shell lines instead of radius amplitude)

### betterposter

<figure>
    <img src="../../../../assets/dvss/b751f589-13a5-4bbf-84ee-85a58c275b50.png" alt="Uploaded image" />
    <figcaption>https://mitcommlab.mit.edu/be/2023/09/27/toward-an-evenbetterposter-improving-the-betterposter-template/</figcaption>
</figure>

### Our World In Data

<figure>
    <img src="../../../../assets/dvss/9e2ed84e-30f3-489a-a816-302714dfc450.png" alt="Uploaded image" />
    <figcaption>https://ourworldindata.org/brief-history-of-ai</figcaption>
</figure>

## Data Visualization

- Anscombe's quartet

### John Snow

<figure>
    <img src="../../../../assets/dvss/31fb8f0a-e452-45fb-a644-9429d854ec82.jpg" alt="Uploaded image" />
    <figcaption>https://storymaps.arcgis.com/stories/59a6e61a0a61448699f67e29bd45714c</figcaption>
</figure>

### Ed Hawkins

<figure>
    <img src="../../../../assets/dvss/a3fcdd24-662e-4112-9388-a50ddbedeaf4.png" alt="Uploaded image" />
    <figcaption>https://showyourstripes.info/</figcaption>
</figure>

### Guidelines for data viz

from ["Better Data Visualization"](https://cup.columbia.edu/book/better-data-visualizations/9780231193115/)

#### 1. Show the data

- sometimes is enough (e.g. spatial data)

#### 2. Reduce the clutter

- avoid useless visual elements (i.e. which don't convey additional information)

<figure>
    <img src="../../../../assets/dvss/b1b173fc-4a06-40cd-af73-aaa74aed329d.png" alt="Uploaded image" />
    <figcaption>https://datavizproject.com/data-type/bar-chart/</figcaption>
</figure>

#### 3. Integrate graphics and text

- legend can be placed close to data traces (ref. proximity)
- title, subtitle, text annotations
- choose an appropriate colormap (e.g. default `jet` colormap in Windy for temperature, which is not a gradient of anything)
- [The misuse of colour in science communication](https://www.nature.com/articles/s41467-020-19160-7)

<figure>
    <img src="../../../../assets/dvss/825e60fb-7243-4930-9e9e-855d94d913c8.webp" alt="Uploaded image" />
    <figcaption>ADD_CAPTION_HERE</figcaption>
</figure>

- avoid inconsistencies (e.g. legend data sorted differently from data traces)
- add explainers (e.g. clearly state what the takeaway should be)
- chart-in-chart to explain details (zoom-in effect)
- explain how to read the graph

<figure>
    <img src="../../../../assets/dvss/ce8249a9-0db9-47f7-8c25-7ecb223e8e81.webp" alt="Uploaded image" />
    <figcaption>https://nightingaledvs.com/connected-scatterplots-make-me-feel-dumb/</figcaption>
</figure>

#### 4. Avoid spaghetti charts

- multivariate data can be visualized as a collection of univariate charts (e.g. linecharts in a grid, with fixed axes ranges)

#### 5. Start with gray

- start with everything in the background, and let emerge the important elements only

## Visual perception and design principles

### [Gestalt principles](https://www.gestaltprinciples.com/)

#### 1. Proximity

- closeness

#### 2. Similarity

- shapes

#### 3. Closure

- tendency to perceive elements even if they are not visible

#### 4. Common fate

- movement

#### 5. Continuity

#### 6. Good figure (Prägnanz)

- visual perception privilege simple and "good" shapes

#### 7. Past experience

### Encoding information

<figure>
    <img src="../../../../assets/dvss/d19312da-b7cd-4dfa-a064-4be5c865e059.png" alt="Uploaded image" />
    <figcaption>https://www.datavizhandbook.info/</figcaption>
</figure>

### Color

- [Chroma.js Color Palette Helper](https://gka.github.io/palettes/#/9|s|00429d,96ffea,ffffe0|ffffe0,ff005e,93003a|1|1)

### Typography

- [The Equilateral Triangle of a Perfect Paragraph](https://betterwebtype.com/triangle/)

## Resources

- [A Comprehensive Guide to Unlocking Your Data's Potential](https://data.europa.eu/apps/data-visualisation-guide/)
- [Royal Statistical Society Best Practices for Data Visualisation](https://royal-statistical-society.github.io/datavisguide/)
















