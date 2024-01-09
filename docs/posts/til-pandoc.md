---
date: 2024-01-08
authors:
  - silvio
categories:
  - TIL
---

# Convert a markdown file to docx with pandoc

Today I rediscover an amazing tool: [pandoc](https://pandoc.org/), which correctly presents itself as

> _your swiss-army knife to convert files from one markup format into another_.

In these days I am working on the redaction of a complex tender notice, which must be delivered as an editable `docx` and then exported (with all the fancy stuff and theming) into `pdf`. Unfortunately, I find the user experience of writing documents with Microsoft Word really unsatisfying and cluttered.

<!-- more -->

Therefore I decidef to project this task to a space where I feel more comfortable: markdown editing. In doing so, I also took the chance to explore a nice tool I discovered some months ago: [Obsidian](https://obsidian.md/).

!!! question "Elephant in the room"
    The main question obviously was: can I easily (and perhaps nicely?) convert my markdown sources into the requested docx format?

Pandoc to the rescue! With an awesome one-liner provided among the documented [examples](https://pandoc.org/demos.html#examples), the conversion takes seconds - and thanks to the `--reference-doc` option the output theming is enforced.

```bash
pandoc --reference-doc reference.docx -o output.docx obsidian_vault/input.md
```

Of course, the above one liner has been already listed as a target into the project [Makefile](/data-scientist-hub/2020/06/11/a-brief-guide-to-gnu-make/).
