#Write a Python function to flatten a nested dictionary.# The function should take a nested dictionary and return a flat dictionary
# where the keys are the concatenation of the nested keys, separated by a specified separator (default is '.').
# For example, given the input {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': 4},
# the output should be {'a.b.c': 1, 'a.b.d': 2, 'a.e': 3, 'f': 4}.
# The function should handle any level of nesting.

def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

nested_dict = {
    "a": {
        "b": {
            "c": 1,
            "d": 2
        },
        "e": 3
    },
    "f": 4
}

flattened = flatten_dict(nested_dict)
print(flattened)
