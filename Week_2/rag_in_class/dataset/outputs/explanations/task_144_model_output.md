# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    total = 0
    for i in range(n - 1, -1, -1):
        total += i * arr[i] - (n - 1 - i) * arr[i]
    return total
```

- Preserved the exact function signature and return type
- Maintained the original loop structure and iteration order
- Kept the identical arithmetic expression for each element
- Preserved the backward iteration from `n-1` down to `0`
- Ensured the same mathematical operations and variable usage
- Returned the accumulated sum exactly as the original
- No changes to edge-case handling or control flow
