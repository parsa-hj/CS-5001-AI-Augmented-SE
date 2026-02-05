# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1, n2):
    return sum(map(int, str(abs(n1 - n2))))
```

- Preserved the exact function signature and return type
- Maintained the same algorithmic steps: absolute difference, string conversion, digit sum
- Kept the same control flow and early operations
- Preserved the exact output for all test cases
- No changes to edge-case behavior
- No additional features or validations added
- Formatting improved for readability while keeping logic identical
