# Jupyter

## autoreload

```python
%load_ext autoreload
%autoreload 2
```

## profiling

```
%load_ext line_profiler

def function_to_profile(arg: int):
    ...

%lprun -f function_to_profile function_to_profile(1)
```

For reference see [here](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html) and [here](https://ipython-books.github.io/43-profiling-your-code-line-by-line-with-line_profiler/).
