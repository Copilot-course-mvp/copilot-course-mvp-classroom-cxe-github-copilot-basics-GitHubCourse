# Usage Guide

## Quickstart

### chunk_list

Split a list into consecutive chunks of a given size:

```python
from exercise import chunk_list

chunks = chunk_list([1, 2, 3, 4, 5], 2)
print(chunks)  # [[1, 2], [3, 4], [5]]
```

### moving_average

Compute a moving average over a sliding window:

```python
from exercise import moving_average

averages = moving_average([10.0, 20.0, 30.0, 40.0], 3)
print(averages)  # [20.0, 30.0]
```

## Edge Cases

- **`chunk_list` with size larger than the list** returns a single chunk:
  ```python
  chunk_list([1, 2], 10)  # [[1, 2]]
  ```

- **`chunk_list` with size of 0 or negative** raises `ValueError`.

- **`moving_average` with window larger than list** returns an empty list:
  ```python
  moving_average([1.0], 5)  # []
  ```

- **`moving_average` with window of 0 or negative** raises `ValueError`.

- **Empty input list**: `chunk_list([], 3)` returns `[]` and `moving_average([], 2)` returns `[]`.
