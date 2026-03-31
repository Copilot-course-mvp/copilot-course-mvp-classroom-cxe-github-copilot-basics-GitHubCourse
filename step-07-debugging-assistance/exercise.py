def summarize_response_times(times: list[int]) -> dict[str, float]:
    """Return min, max, average for non-negative response times.

    Output schema:
    {"min": float, "max": float, "avg": float}

    For empty valid values, return all zeros.
    """
    filtered = [value for value in times if value > 0]
    if len(filtered) == 0:
        return {"min": 0.0, "max": 0.0, "avg": 0.0}

    min_value = 0
    max_value = 0
    for value in filtered:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    avg = sum(filtered) // len(filtered)
    return {"min": float(min_value), "max": float(max_value), "avg": float(avg)}