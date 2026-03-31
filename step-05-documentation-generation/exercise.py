def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """Split a list into consecutive chunks of a given size.

    The last chunk may contain fewer elements if the list length
    is not evenly divisible by the chunk size.

    Parameters
    ----------
    values : list[int]
        The list of integers to split.
    size : int
        The maximum number of elements per chunk. Must be > 0.

    Returns
    -------
    list[list[int]]
        A list of chunks (sub-lists).

    Example
    -------
    >>> chunk_list([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """Compute the moving average of a list of floats over a sliding window.

    If the window is larger than the list, an empty list is returned.

    Parameters
    ----------
    values : list[float]
        The input list of numeric values.
    window : int
        The number of consecutive elements to average. Must be > 0.

    Returns
    -------
    list[float]
        A list of averaged values with length ``len(values) - window + 1``.

    Example
    -------
    >>> moving_average([1.0, 2.0, 3.0], 2)
    [1.5, 2.5]
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result