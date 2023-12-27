# sklearn

## `TimeSeriesSplitMultiStep`

```python
import numpy as np
import pandas as pd
from sklearn import model_selection


def TimeSeriesSplitMultiStep(series: pd.DataFrame, 
                             n_splits: int = 3, 
                             n_steps: int = 3, 
                             max_train_size: Optional[int] = None) -> tuple:
    """Extend sklearn' TimeSeriesSplit to the multistep case.

    Args:
        series (pd.DataFrame): input time series.
        n_splits (optional, int): number of splits. Defaults to 3.
        n_steps (optional, int): number of steps ahead. Defaults to 3.
        max_train_size (optional, Optional[int]): maximum training set size. Defaults to None.

    Returns:
        Indices for splitting.
    """
    tscv = model_selection.TimeSeriesSplit(n_splits, max_train_size)

    for train_index, test_index in tscv.split(series):
        last_test_index = test_index[-1]
        step_to_add = n_steps - len(test_index)
        if last_test_index < len(series) - step_to_add:
            if step_to_add > 0:
                for next_step in range(last_test_index + 1, step_to_add + last_test_index + 1):
                    test_index = np.append(test_index, next_step)
            yield train_index, test_index
```
