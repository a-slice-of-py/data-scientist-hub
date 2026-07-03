---
date: 2026-07-03
authors:
  - silvio
categories:
  - Prompts
---

# Resource Curator

Here is the prompt I use within the [Agentic IDE Kiro](https://kiro.dev/ide/)[^1] to manage the insertion of new resources into DSH.

[^1]: I mostly use it in _auto mode_, where a bunch of underlying LLMs (mostly from Anthropic) are orchestrated in the "most token-efficient way".

<!-- more -->

## Knowledge base organization

The following repo implements my personal knowledge platform about data topics. In particular, in `docs/resources` there is a curated (yet opinionated) collection of links to useful online resources.

The resources are organized in the following subfolders:

- **AWS**: Amazon Web Service related stuff.
- **Career**: how to shape a data career and nail down job interviews!
- **Data Engineering**: data architectures, monitoring and observability, DevOps and others data engineering best practices.
- **Data Science**: data science, in the widest meaning of the term.
- **Data Visualization**: information and data visualization, both methodology and implementation.
- **Education**: collection of resources for an effective data education.
- **Misc**: a salad of math, physics and the rest of hard sciences.
- **Python**: Python, my actual programming language.
- **Tools**: toolbox full of utilities.
- **Training**: books, MOOC, certifications and everything else about training.

I want you to perform the following two task, where task 2 depends on task 1.

## Task 1: enrich raw links

I want you to go through the raw links in `tmp.md` (located at the repo root). Each line contains a single URL with no additional text. I want you to:

- transform each link in markdown format and as an element of a list, i.e. `- [LINK_LABEL](LINK_URL)`
- fill each markdown link label based on URL name

### Labeling criteria

- For **GitHub repos**: fetch the repo description (or first line of README) and format as `[repo-name: brief description](url)`, via webfetch or non-authenticated github api
- For **articles/blogs/docs**: use the page `<title>` tag as link label
- For **YouTube videos**: use the video title
- For **PDFs**: use the document title or filename if title is unavailable
- For all labels: capitalize the first letter, replace hyphens/underscores with spaces

## Task 2: copy enriched links

Copy each of the curated link enriched via task 1 into the most relevant markdown under `docs/resources` folder. Please note that:

- in resources folder there are subfolders for categories, e.g. `docs/resources/data-science`
- in each folder there are several markdown (e.g. `docs/resources/data-science/clustering.md`), and these markdown can have inner sections defined by subheaders
- you must choose the best subfolder, markdown and section to copy each of the link into

### Placing criteria

- NEVER copy to markdown in `docs/resources/changelog` or `docs/resources/snippets` (you can entirely skip these folders)
- Append new links at the end of the relevant section (or at the end of the file if no sections exist).
- Choose the most specific existing section that matches the link's topic.
- If no section fits well, append to the bottom of the most relevant file under a new section header.
- If a link already exists in the target location, skip it (no duplicates).
- If a link could belong to multiple categories, prefer the more specific one (e.g. `clustering.md` over a general `machine-learning.md`).

## Success criteria

1. Each raw link in `tmp.md` must be enriched
2. Each enriched links in `tmp.md` must be copied to exactly one target resource markdown file (no orphans, no duplicates)
3. `tmp.md` must be left with enriched links at the end of the workflow.
