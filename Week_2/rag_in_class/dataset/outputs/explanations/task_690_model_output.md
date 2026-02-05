# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list."""
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
```

- Preserved the exact function signature and return type
- Maintained the original list comprehension logic for multiplying consecutive pairs
- Kept the same behavior for edge cases (empty list, single element list)
- Used the same variable names to avoid any semantic changes
- Preserved the exact output format (list of products)
- No changes to the algorithm or control flow
- All test cases should pass without modification
