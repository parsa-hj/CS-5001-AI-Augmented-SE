# Model output for task_488

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

## Refactored Code:

```python
import math

def area_pentagon(a):
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
```

- Preserved the exact formula for calculating the area of a regular pentagon
- Maintained the same mathematical operations and order of calculations
- Kept the return type and value unchanged
- Used the same floating-point division (4.0) as in the original
- Preserved the use of `math.sqrt` and `pow` functions
- No changes to function signature or behavior
- All edge cases (e.g., negative inputs, zero) will behave identically to the original
