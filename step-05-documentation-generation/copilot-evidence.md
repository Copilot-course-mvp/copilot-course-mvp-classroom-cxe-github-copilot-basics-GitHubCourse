# Copilot Evidence — Step 05

## Documentation prompt

Asked Copilot to generate NumPy-style docstrings for `chunk_list` and `moving_average` including Parameters, Returns, and Example sections. Also asked to generate a USAGE.md with quickstart and edge case documentation.

## What you edited after Copilot output

Refined the edge case section in USAGE.md to include specific examples for boundary conditions like window larger than list and zero/negative size values.

## Accuracy check

Verified documentation matches actual behavior by running the example code snippets and comparing outputs. Confirmed that ValueError is raised for invalid size/window parameters as documented.
