
# Copilot Evidence — Step 01

    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name

    title = title.strip()
    title = title.lower()
    title = re.sub(r'[^a-z0-9]+', '-', title)
    title = title.strip('-')
    return title
## Prompt 1

Complete this function to normalize usernames following the rules in the docstring.

## Why you accepted/rejected the suggestion
It looked like it was able to transform the string according to the instructions I´m not familiar with python but also looked in the chat how a function like that one would look like

## Final check
I accepted the suggestions on the first try.