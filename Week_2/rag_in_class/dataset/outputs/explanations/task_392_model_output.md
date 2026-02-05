# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]))
    return res[n]
```

- Preserved the exact function signature and return type
- Maintained the same initialization of `res` with `[0, 1]`
- Kept the same loop bounds (2 to n inclusive)
- Preserved the exact calculation logic using integer division
- Maintained the same max operation between `i` and the sum of previous values
- Kept the same return value `res[n]`
- Improved readability by using a for loop and removing redundant variable `i` increment
- Preserved all edge cases and behavior exactly as in the original implementation
