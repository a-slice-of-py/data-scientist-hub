---
date: 2024-05-16
authors:
  - silvio
categories:
  - TIL
tags:
  - Python
---

# Three Python libraries for/with a great user experience

I am working on a super-opinionated solution to assume AWS roles via STS, both programmatically and to log into AWS Console. While searching in the Python ecosystem utilities to build CLI and GUI with, I discovered three libraries that offer a great user experience both _for_ the end users and the developers that build _with_ them.

<!-- more -->

These libraries are:

- [Dear PyGui](https://github.com/hoffstadt/DearPyGui), a fast and powerful GUI toolkit with minimal dependencies, which offers great documentation and an awesome [demo](https://github.com/hoffstadt/DearPyGui?tab=readme-ov-file#demo) from which is very easy to steal ideas and working snippets[^1];
- [Questionary](https://github.com/tmbo/questionary), the missing piece for building interactive CLI in Python;
- [Termynal](https://github.com/termynal/termynal.py), a "Python markdown terminal" built for mkdocs, very useful to include in tools documentation following [show don't tell](https://en.wikipedia.org/wiki/Show,_don%27t_tell) approach.

[^1]: One of the few libraries I found outside the "web application builder" framework that offers the same fresh ux.
