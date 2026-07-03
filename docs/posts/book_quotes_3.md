---
date: 2023-12-27
authors:
  - silvio
categories:
  - QFTB
---

# Quotes From The Book - part 3 - Fluent Python

Over the past two years I had the chance to read a bunch of data-related books on the O'Reilly learning platform: what follows is a collection of quotes from _"Fluent Python, 2nd Edition"_ by Luciano Ramalho that captured my attention or hit hard because they were highly relatable.

<!-- more -->

## Fluent Python, 2nd Edition

### 2. An Array of Sequences

> _Listcomps do everything the map and filter functions do, without the contortions of the functionally challenged Python lambda._

---

> _This example is quite a corner case—in 20 years using Python, I have never seen this strange behavior actually bite somebody._
>
> _I take three lessons from this:_
>
> _Avoid putting mutable items in tuples._
>
> _Augmented assignment is not an atomic operation—we just saw it throwing an exception after doing part of its job._
>
> _Inspecting Python bytecode is not too difficult, and can be helpful to see what is going on under the hood._

### 5. Data Class Builders

> _If a class is widely used but has no significant behavior of its own, it’s possible that code dealing with its instances is scattered (and even duplicated) in methods and functions throughout the system—a recipe for maintenance headaches. That’s why Fowler’s refactorings to deal with a data class involve bringing responsibilities back into it._

### 6. Object References, Mutability, and Recycling

> _Usually we are more interested in object equality than identity. Checking for None is the only common use case for the is operator. Most other uses I see while reviewing code are wrong. If you are not sure, use ==. It’s usually what you want, and also works with None—albeit not as fast._

### 7. Functions as First-Class Objects

> _Another group of one-trick lambdas that operator replaces are functions to pick items from sequences or read attributes from objects: itemgetter and attrgetter are factories that build custom functions to do that._

---

> _The operator module provides function equivalents for dozens of operators so you don’t have to code trivial functions_

### 9. Decorators and Closures

> _Similar decorators are used in many Python frameworks to add functions to some central registry_

---

> _A key feature of decorators is that they run right after the decorated function is defined. That is usually at import time (i.e., when a module is loaded by Python)_

---

> _A notable quality of the singledispatch mechanism is that you can register specialized functions anywhere in the system, in any module. If you later add a module with a new user-defined type, you can easily provide a new custom function to handle that type._

---

> _Besides making silly recursive algorithms viable, @cache really shines in applications that need to fetch information from remote APIs._

### 17. Iterables, Iterators, and Generators

> _Understanding classic coroutines in Python is confusing because they are actually generators used in a different way._

