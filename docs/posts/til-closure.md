---
date: 2024-01-24
authors:
  - silvio
categories:
  - TIL
tags:
  - Python
  - AWS
---

# All you need is closure

Decorators are well known examples of Python [**syntactic sugar**](https://en.wikipedia.org/wiki/Syntactic_sugar#Notable_examples), which basically let you change the behaviour of a function without modifying its definition, thanks to a handy syntax based on the `@` symbol followed by the decorator name, everything put just above your function definition.

Sometimes, however, you can't exploit this syntax, for example because you don't have the function definition at your disposal - let's think at the case in which the function you want to decorate lives in another codebase (the latter might be one of the libraries your project depends on).

<!-- more -->

The syntactic sugar approach, generally speaking, gives a lot of advantages in terms of experimentation, reusability and reversibility. However, in cases like the ones mentioned above, this approach can do more harm than good, forcing you to wrap a function invocation in another function with the only aim of providing _a function definition_ to decorate, with the risk of reduce the readability and maintainability of your codebase[^1].

What you can do instead is take a step back and use the decorator function directly for what it is: a [**closure**](https://en.wikipedia.org/wiki/Closure_(computer_programming))[^2].

=== "Scenario"

    ```python    
    from external_lib import some_func

    def main():
        # ... complex logic that you can't refactor
        # which defines inputs for some_func  ...
        response = some_func(inputs)
    ```

=== "Closure approach"

    ```python
    from external_lib import some_func

    def decorator(func):
        # ... custom logic ...

    def main():
        # ... complex logic that you can't refactor
        # which defines inputs for some_func  ...
        response = decorator(some_func)(inputs)
    ```

=== "Syntactic sugar approach"

    ```python
    from external_lib import some_func

    def decorator(func):
        # ... custom logic ...

    def main():
        # ... complex logic that you can't refactor
        # which defines inputs for some_func  ...
        @decorator
        def pointless_wrapper():
            return some_func(inputs)
        
        response = pointless_wrapper()
    ```

## A real world example

I came across the above reasonings while I was working on error handling in a serverless architecture based on AWS.

Specifically, my need was to catch and retry a specific error raised by [awswrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/index.html) (aws-sdk-pandas) when an Athena query execution fails i.e., `awswrangler.exceptions.QueryFailed`. This error is often raised by [`awswrangler.athena.read_sql_query`](https://aws-sdk-pandas.readthedocs.io/en/stable/stubs/awswrangler.athena.read_sql_query.html) or [`awswrangler.athena.start_query_execution`](https://aws-sdk-pandas.readthedocs.io/en/stable/stubs/awswrangler.athena.start_query_execution.html), the latter being used with `wait=True`.

I recently read and enjoy [Robust Python by Patrick Viafore](https://learning.oreilly.com/library/view/robust-python/9781098100650/) - which I totally recommend to seasoned Python developers, for a lot of reasons far beyond the scope of this post - where the author recommends the [`backoff`](https://github.com/litl/backoff) library for such tasks.

Backoff offers a handy decorator-based approach to handle retry logic in a wide range of different situations, with some customization options to be feed as decorator kwargs.

Thanks to the intuitive and well documented API, after few minutes of experiments I converge to this setup which seemed to do the job:

```python
import awswrangler as wr
import backoff

@backoff.on_exception(backoff.expo, wr.exceptions.QueryFailed, max_tries=3)
```

I was ready to add the customized decorator to my codebase, but I then realized that I do not have access to awswrangler.athena functions _definition_. I suddenly found myself wondering whether or not I can decorate function _invocation_ instead: a quick Google search gave me the simple (yet forgotten) [answer](https://stackoverflow.com/questions/39370642/python-decorate-function-call).

All I had to do was aliasing my custom decorator and then use it wherever required by simply wrapping original function call with the defined alias[^3].

=== "Before"

    ```python
    import awswrangler as wr

    response = wr.athena.read_sql_query(sql, database)
    ```

=== "After"

    ```python
    import awswrangler as wr
    import backoff

    retry_when_query_fails = backoff.on_exception(
        backoff.expo,
        wr.exceptions.QueryFailed,
        max_tries=3
    )

    response = retry_when_query_fails(wr.athena.read_sql_query)(sql, database)
    ```

[^1]: This can be referred to as [_syntactic diabetes_](https://www.google.com/search?q=synctatic+diabetes).
[^2]: This [blog post](https://aviadr1.github.io/learn-advanced-python/02_closures_and_decorators/closure_and_decorators.html) gives well explained details about both closures and decorators in Python.
[^3]: Since backoff library exposes functions which can be used as decorators, this ensures that they also can be used as plain closures.
