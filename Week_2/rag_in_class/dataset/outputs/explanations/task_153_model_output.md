# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x = (-b) / (2 * a)
    y = ((4 * a * c) - (b * b)) / (4 * a)
    return (x, y)
```

- Preserved exact function signature and return type
- Maintained identical calculation for x-coordinate of vertex
- Preserved exact formula for y-coordinate calculation
- Kept tuple return structure unchanged
- Preserved all floating-point arithmetic behavior
- No changes to edge-case handling or control flow
- Improved readability through variable naming without altering logic
