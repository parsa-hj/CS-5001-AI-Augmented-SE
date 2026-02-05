# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)
    for char in char_order:
        if char_count[char] == 1:
            return char
    return None
```

- Renamed `ctr` to `char_count` for better readability while preserving exact behavior
- Renamed `c` to `char` for clarity in loop variables
- Maintained identical logic flow and return conditions
- Preserved the exact same dictionary and list operations
- Kept the same return values (including `None` for no match)
- All edge cases (empty string, all repeats, etc.) handled identically
- No changes to function signature or return types
