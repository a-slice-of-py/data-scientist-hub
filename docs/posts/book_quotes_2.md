---
date: 2023-12-23
authors:
  - silvio
categories:
  - QFTB
---

# Quotes From The Book - part 2 - Robust Python

Over the past two years I had the chance to read a bunch of data-related books on the O'Reilly learning platform: what follows is a collection of quotes from _"Robust Python"_ by Patrick Viafore that captured my attention or hit hard because they were highly relatable.

<!-- more -->

## Robust Python

### 1. Introduction to Robust Python

> _Asynchronous communication means that producing information and consuming that information are independent of each other._

---

> _The Law Of Least Surprise, also known as the Law of Least Astonishment, states that a program should always respond to the user in the way that astonishes them the least.3 Surprising behavior leads to confusion. Confusion leads to misplaced assumptions. Misplaced assumptions lead to bugs. And that is how you get unreliable software._

---

> _When you pick a collection, you are communicating specific information. You must pick the right collection for the task at hand. Otherwise, maintainers will infer the wrong intention from your code._

---

> _You need to express intent in your code up front_

---

> _your code is one of your best documentation tools, as it is the living record and single source of truth for your system_

---

> _some common communication methods’ cost and proximity required_

### 2. Introduction to Python Types

> _Duck typing is the ability to use objects and entities in a programming language as long as they adhere to some interface._

---

> _Dynamic typing, on the other hand, embeds type information with the value or variable itself. Variables can change types at runtime quite easily, because there is no type information tied to that variable._

---

> _Languages that offer static typing embed their typing information in variables during build time. Developers may explicitly add type information to variables, or some tool such as a compiler infers types for the developer. Variables do not change their type at runtime (hence, “static”)._

---

> _In contrast, languages toward the weaker side of the spectrum will not restrict the use of operations to the types that support them. Types are often coerced into a different type to make sense of an operation._

---

> _Languages toward the stronger side of the spectrum tend to restrict the use of operations to the types that support them. In other words, if you break the semantic representation of the type, you are told (sometimes quite loudly) through a compiler error or a runtime error_

---

> _Python falls toward the stronger side of the spectrum. There are very few implicit conversions that happen between types_

### 3. Type Annotations

> _Typecheckers start giving us the benefit of a statically typed language, while still allowing the Python runtime to remain dynamically typed._

---

> _When should you use typecheckers?_

### 4. Constraining Types

> _Literal types allow you to restrict the variable to a very specific set of values._

---

> _It is important to notify users that the only way to create your new type is through a set of “blessed” functions. You don’t want users creating your new type in any circumstance other than a predetermined method, as that defeats the purpose._

---

> _your code will be flagged when your dependencies change in a way that contradicts your assumptions. With the decisions you make today, you can catch errors in the future. This is the mark of robust code;_

---

> _This isn’t to say don’t use exceptions. Use them for exceptional use cases that you don’t expect to happen, but still wish to guard against, such as the network going down. Don’t use exceptions for normal behavior, such as not finding an element when searching through a list._

### 5. Collection Types

> _That’s the beauty of collections.abc. Once you define a select few methods, the rest come for free_

---

> _In order to create a custom collection, you must override specific functions, depending on the type you want to emulate. Once you implement these required functions, though, the ABC fills in other functions automatically. You can find a full list of required functions to implement at the collections.abc's module documentation._

---

> _UserDict isn’t the only collection type that you can override in this case. There also is a UserString and a UserList in the collections model. Anytime you want to tweak a dictionary, string, or list, these are the collections you want to use._
>
> _WARNING_
> _Inheriting from these classes does incur a performance cost._

---

> _You have to specify a Union[X, APIError] each time, where only X changes._

---

> _TypedDict, introduced in Python 3.8, is for the scenarios where you absolutely must store heterogeneous data in a dictionary. These are typically situations where you can’t avoid heterogeneous data. JSON APIs, YAML, TOML, XML, and CSVs all have easy-to-use Python modules that convert these data formats into a dictionary and are naturally hetereogeneous._

---

> _dictionaries are typically meant to be a homogeneous mapping from a key to a value_

### 6. Customizing Your Typechecker

> _Pylance has a setting that allows you to constantly run diagnostics in your whole workspace. This means that every time you edit a file, pyright will run across your entire workspace (and it runs fast, too) to look for additional areas that you broke. You don’t need to manually run any commands; it happens automatically._

---

> _two other typecheckers: Pyre (written by Facebook) and Pyright (written by Microsoft)._

---

> _You also should consider mypy in daemon mode. Daemon mode is when mypy runs as a standalone process, and keeps the previous mypy state in memory rather than on a file system (or across a network link)._

---

> _a beautifully concise definition of typecheckers: “In essence, [a typechecker] provides verified documentation._

### 7. Adopting Typechecking Practically

> _MonkeyType is a tool that will automatically annotate your Python code._

---

> _One of the problems with MonkeyType is that it only annotates code it sees at runtime. If there are branches of your code that are costly or unable to be run, MonkeyType will not help you that much. Fortunately, a tool exists to fill in this gap: Pytype, written by Google. Pytype adds type annotations through static analysis, which means it does not need to run your code to figure out types._

---

> _One of the biggest problems you will run into is the sheer number of errors that mypy will report the first time you run it on a larger codebase. The biggest mistake you can make in this situation is to keep the hundreds (or thousands) of errors turned on and hope that developers whittle away at the errors over time._

---

> _this is where the amount of effort that you’re expending is paid back by the value you are receiving. You want to reach this point as fast as sustainably possible so that your type annotations have a positive impact. Here are some strategies to do that._

---

> _Adopting type annotations is not free. Worse, with a large enough codebase, these costs can easily dwarf the initial benefit you get from typechecking._

---

> _Most of the type annotation strategies that I’ve shown in the first part of this book are easier to adopt when a project is new. Adopting these practices in a mature project is more challenging. It is not impossible, but the cost may be higher. This is the heart of engineering: making smart decisions about trade-offs._

---

> _Feathers defines legacy code as “code without tests.” I prefer an alternate definition: legacy code is simply code where you can no longer discuss the code with the developers who wrote it._

### 8. User-Defined Types: Enums

> _if you want to preserve uniqueness in your Enum, simply add a @unique decorator._

---

> _Enumerations are great for communicating a static set of choices for users._

### 9. User-Defined Types: Data Classes

> _However, as great as data classes are, they should not be universally used. A data class, at its heart, represents a conceptual relationship, but it really is only appropriate when the members within the data class are independent of one another. If any of the members should be restricted depending on the other members, a data class will make it harder to reason about your code._

---

> _a frozen dataclass only prevents its members from being set. If the members are mutable, you are still able to call methods on those members to modify their values. frozen dataclasses do not extend immutability to their attributes._

---

> _To freeze a dataclass, add a frozen=True to the dataclass decorator:_

---

> _If you override comparison functions, do not specify order=True, as that will raise a TypeError._

---

> _If you want to control how comparison is defined, you can write your own __le__, __lt__, __gt__, and __ge__ functions in the dataclass, which map to less-than-or-equals, less-than, greater-than, and greater-than-or-equals, respectively._

---

> _If you want to be able to define relational comparison (<, >, <=, >=), you need to set eq=True and order=True in the dataclass definition._

### 10. User-Defined Types: Classes

> _decorators that allow you to write functions that are bound to a class instead of an instance (classmethod) and functions that live inside a class but aren’t bound to it in any way (staticmethod). To me, these are holdovers from an older mentality of programming where there weren’t as many robust patterns as there are today_

---

> _If you have functions that don’t concern themselves with invariants, or even worse, don’t concern themselves with members of the class, you probably have a free function instead_

---

> _Protected and private attributes don’t show up in help() of a class. This will reduce the chance of somebody using these attributes inadvertently. Furthermore, private attributes aren’t as easily accessible._

---

> _Public and protected attributes form your public API, and should be relatively stable before people depend on your class heavily. However, it is a general convention that people should leave your private API alone_

---

> _Encapsulation. Simply put, it’s the ability for an entity to hide properties and the actions that operate upon those properties._

---

> _You should absolutely write unit tests around your expectations and invariants, but there’s one additional facet I’d like you to consider: help future test writers know when invariants are broken as well._

---

> _code should absolutely self-document what it’s doing (this is just another spin on the Law of Least Surprise), but comments help the human nature of code. Most people simplify this to why the code behaves it does_

---

> _If you answer yes to any of these questions, you have invariants you want to preserve and should write a class._

---

> _If you really want to, you can move your invariant checking to the function itself, but at that point, you are dealing with an invariant-less type and you should be using a data class. If you are more accustomed to functional programming paradigms, and will be keeping most of your classes immutable, then this is less of an issue_

---

> _Assertions are not guaranteed to execute at runtime, as your code may be deployed with options that disable assertions. In this case, I use them for things that I always expect to be true, unless a developer in the system messes up. It is intended to catch mistakes during development, and it signals to other developers that it is up to them to not create a situation that fails an assertion._
>
> _Exceptions, on the other hand, indicate to a developer that something may be possible due to user error or malicious actors. It is unlikely to happen, but other developers must be prepared to catch the exception if something goes wrong._

---

> _a class can convey one key thing that a dictionary or data class can’t easily convey: invariants_

---

> _But you might (rightly) wonder why you would ever use a class instead of a data class again?_

### 11. Defining Your Interfaces

> _You are eliminating an entire class of errors that can happen when you use context managers—the errors of omission. Errors of omission are so easy to make; you literally have to do nothing. Instead, a context manager lets users do the right thing, even when they do nothing. It’s a sure sign of a robust codebase when a user can do the right thing without even knowing it_

---

> _When the with block exits, execution is returned to the context manager, right after the yield statement. It doesn’t matter if an exception is thrown, or if the with block finishes normally; because I wrapped our yield in a try...finally block,_

---

> _Wanting to automatically invoke some sort of function when you are done with an operation is a common case in Python._

---

> _Common magic methods in Python_

---

> _Just as your code is a single source of truth for the behavior in your system, your tests are the single source of truth for interacting with your code._

---

> _thinking of TDD as a testing methodology, when in fact, it is a design methodology. The tests are important, but they are merely a by-product of the methodology. The true value lies in how tests help design your interface_

### 12. Subtyping

> _Composition is preferable to inheritance as a reuse mechanism because it is a weaker form of coupling, which is another term for dependencies between entities. All other things being equal, you want weaker forms of coupling, as it makes it easier to reorganize classes and refactor functionality. If classes have high coupling between them, changes in one more directly affect the behavior of the other._

---

> _you want to use composition, also known as a has-a relationship. Composition is when you put member variables inside a type._

---

> _If a supertype defines postconditions, the subtype must not weaken those postconditions._

---

> _If the supertype defines preconditions that happen, the subtype must not be more restrictive._

---

> _When you’re subtyping from other types, the subtypes must preserve all invariants._

---

> _Substitutability states that when you derive from a base class, you should be able to use that derived class in every instance that you use a base class._

---

> _there is one case that I am fond of for multiple inheritance: mixins. Mixins are classes that you can inherit generic functionality from. These base classes typically do not contain any invariants or data; they are just a set of methods that are not intended to be overridden_

### 13. Protocols

> _classes subclassed from a protocol do not automatically become a protocol_

---

> _Anything subclassing another class or adhering to a protocol is a subtype. Therefore, it needs to uphold the contract of the parent type. If the contract just defines the structure of the type (such as being Splittable, which just needed certain attributes to be defined), use a protocol. However, if the parent type’s contract defines behaviors that need to be upheld, such as how to operate in certain conditions, use inheritance to better reflect the is-a relationship_

---

> _I want to be able to have typing work based on the structure of the code. To do this, you can define your own protocol._

### 14. Runtime Checking With pydantic

> _while pydantic advertises itself as a parsing library, it is possible to enforce more strict behavior in your data models_

---

> _Pydantic advertises itself as a parsing library, which means it is providing a guarantee of what comes out of the data model, not what goes in._

---

> _Pydantic offers a ton of built-in validators._

### 16. Dependencies

> _tools exist to help you make sense of your dependencies visually._

---

> _Temporal dependencies bite you the most in situations where you must do certain operations in a specific order, but you have no indication that you need to do so._

---

> _Whenever you create a dependency on something that is not directly apparent in code, find a way to make it apparent. Leave a trail of breadcrumbs, preferably with a separate codepath (like the intermediary function above) or types. If you can’t do that, leave a comment._

---

> _This is the trade-off of introducing a logical dependency. You increase maintainability by increasing substitutability and reducing coupling, but you also decrease maintainability by making your code harder to read and understand._

---

> _The key benefit for introducing a logical dependency is substitutability. It is much easier to replace a component when nothing is physically depending on it._

---

> _It’s possible for the DRY principle to go too far, though. Every time you refactor code, you are introducing a physical dependency to the refactored code. If other parts of your codebase depend on this piece of code, you are coupling them together. If that refactored central piece of code needs to change, it can affect a large amount of code._
>
> _When applying the DRY principle, don’t deduplicate code just because it looks the same; deduplicate it only if that code has the same reasons to change._

### 17. Composability

> _There is a bevy of composable decorators that you can use to simplify your code_

---

> _When you focus on making code composable, you need to separate the policies from the mechanisms. The mechanisms are often the thing you want to reuse; it doesn’t help when they are linked together with a policy._

---

> _Policies are your business logic, or the code directly responsible for solving your business needs. The mechanisms are the pieces of code that provide how you will enact the policies._

### 18. Event-Driven Architecture

> _Reactive programming is an architectural style that revolves around streams of events. You define data sources as producers of these streams, and then link together multiple observers. Each observer is notified whenever there is a change in data and defines a series of operations for handling the data stream. The reactive programming style was popularized by ReactiveX._

---

> _PATTERNS WITHOUT CLASSES_

---

> _With the Observer Pattern, your producer contains of a list of observers: the consumers in this scenario. The Observer Pattern does not need a separate library to act as a message broker._
>
> _To avoid directly linking producers and consumers, you need to keep the knowledge of observers generic. In other words, keep any specific knowledge about the observers abstracted away. I will do this by just using functions (type annotated as a Callable)_

---

> _PyPubSub is meant for single-process applications; you cannot publish to code running in other processes or systems. Other applications can be used to provide this functionality, such as Kafka, Redis, or RabbitMQ._

---

> _the Python library PyPubSub, which is a publish-subscribe API used in single-process applications._

---

> _Event-driven architectures aim to sever this physical dependency. The goal is to decouple producers and consumers. Producers do not know about the consumers, and consumers do not know about the producers. This is what drives the flexibility of an event-driven architecture._
>
> _With this decoupling, it becomes incredibly easy to add onto your system. If you need new consumers, you can add them without ever touching the producer. If you need different producers, you can add them without ever touching the consumers. This bidirectional extensibility allows you to substantially change multiple parts of your codebase in isolation._

### 19. Pluggable Python

> _the same patterns apply to your architecture as well. Being able to inject classes, modules, or subsystems is just as important. A Python library called stevedore is an incredibly useful tool for managing plug-ins._
>
> _A plug-in is a piece of code that can be dynamically loaded at runtime. Code can scan for installed plug-ins, select an appropriate one, and delegate responsibilities to that plug-in. This is another example of extensibility; developers can focus on specific plug-ins without touching the core codebase._

---

> _The Template Method Pattern is a pattern for filling in the blanks of an algorithm.1 The idea is that you define an algorithm as a series of steps, but you force the caller to override some of those steps_

### 20. Static Analysis

> _There’s another complexity heuristic that I am quite fond of that is a bit simpler to reason about than cyclomatic complexity: whitespace checking. The idea is as follows: count how many levels of indentation there are in a single Python file. High levels of indentation indicate nested loops and branches, which may signal complex code._

---

> _The astroid library is useful for parsing Python files into an abstract syntax tree (AST)._

---

> _One of the common tenets of the DevOps mindset is to “shift your errors left.”_

### 21. Testing Strategy

> _For more complex assertions, build up an assertion library that makes it incredibly easy to define new tests. This is like building a vocabulary in your codebase; you want a diverse set of concepts to share in your test code as well. For this, I recommend using Hamcrest matchers.5_

---

> _If you are using pytest fixtures, you can use them much like you could a context manager. You can yield values from a fixture, allowing you to return to the fixture’s execution after the test finishes._

---

> _When writing a test, it helps for each test to follow the same basic pattern._
>
> _One of the most common patterns you’ll find in tests is the 3A, or AAA, test pattern.4 AAA stands for Arrange-Act-Assert. You break up each test into three separate blocks of code, one for setting up your preconditions (arrange), one for performing the operations that are being tested (act), and then one for checking for any post-conditions (assert). You may also hear about a fourth A, for annihilate, or your clean-up code_

---

> _The cost of a test is threefold: the initial cost of writing, the cost of running, and the cost for maintenance._

---

> _a list of common questions and the appropriate tests that answer those questions._

### 22. Acceptance Testing

> _The Python module behave allows you to back your Gherkin requirements with concrete tests. It does so by associating functions with specific clauses in the requirement._

### 23. Property-Based Testing

> _Rather than writing a slew of test cases, I will represent my tests using a hypothesis.stateful.RuleBasedStateMachine. This will let me test entire algorithms using Hypothesis, while checking for invariants along the way_

---

> _Hypothesis will store examples of failed test cases in a local database (by default, in a folder called .hypothesis/examples under the same directory where you ran the tests). It is known as the example database. This is used for future test invocations to guide Hypothesis in testing common error cases._

---

> _Hypothesis will check new values every time you run this test_

---

> _Property-based testing is a form of generative testing, where tools generate test cases for you._

### 24. Mutation Testing

> _Mutation testing is your best defense against poor assumptions about code coverage. When you are measuring the efficacy of your tests, it becomes much harder to write useless, meaningless tests while still eliminating mutants. Mutation testing elevates coverage measurements to become a truer predictor of robustness. Coverage metrics still won’t be a perfect proxy for business value, but mutation testing certainly makes them more valuable as an indicator of robustness._

---

> _mutmut comes with an option to mutation test only the parts of your codebase that have line coverage. A line of code has coverage by test suite if it is executed at least once by any test._

---

> _If your codebase does not have a mature set of tests, you will see little value in introducing mutation testing. It will end up providing too high of a noise-to-signal ratio. You will see much more value from improving your test suite than trying to find all the mutants._

---

> _mutmut is a Python tool that does mutation testing for you._

---

> _Mutation testing is the act of making changes in your source code with the intent of introducing bugs.1 Each change you make in this fashion is known as a mutant. You then run your test suite. If the tests fail, it’s good news; your tests were successful in eliminating the mutant. However, if your tests pass, that means your tests are not robust enough to catch legitimate failures; the mutant survives. Mutation testing is a form of meta-testing, in that you are testing how good your tests are. After all, your test code should be a first-class citizen in your codebase; it requires some level of testing as well._

