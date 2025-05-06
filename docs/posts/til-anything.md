---
date: 2025-04-18
authors:
  - silvio
categories:
  - TIL
tags:
  - Python
---

# Import anything from a Python module

Today, thanks to [Vincent Warmerdam](https://koaning.io/posts/parsing-python-web-components/), I discover a really neat Python trick.

You can basically import _anything_ from a Python module i.e., any Python object, just by defining the module's `__getattr__` method.

<!-- more -->

The following is a simplified version of what Vincent implemented in [mohtml](https://github.com/koaning/mohtml/blob/main/mohtml/anything.py):

```python
# anything.py

def build_init(class_name):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        if "klass" in self.kwargs:
            self.kwargs["class"] = self.kwargs["klass"]
            del self.kwargs["klass"]

    return __init__


def build_repr(class_name):
    def __repr__(self):
        return f"This is the {class_name} representation."

    return __repr__


def build_docstring(class_name):
    return f"Docstrings of `{class_name}`."


def __getattr__(class_name):
    class_name = class_name.replace("_", "-")
    new_class = type(
        class_name,
        (),
        {
            "__init__": build_init(class_name),
            "__repr__": build_repr(class_name),
            "__doc__": build_docstring(class_name),
            "__str__": build_repr(class_name),
        },
    )

    return new_class
```

With this module you can do things like `from anything import This, That`, with `This` and `That` being Python classes created on-demand which abide by the interface defined in `anything.__getattr__`!

Boom!
