# Model output for task_940

## Model
- devstral-small-2:24b-cloud

## Original Code:

def heap_sort(arr):
    heapify(arr)  
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1
def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

## Refactored Code:

```python
def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1

def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return
```

- Preserved all function names, argument lists, and return types exactly as in the original
- Maintained the same control flow and logic in heap_sort, heapify, and shift_down
- Kept the exact same variable names and loop structures to ensure identical behavior
- Preserved the original edge-case handling (e.g., empty arrays, single-element arrays)
- Ensured the same swapping and comparison logic in shift_down
- Did not add any new features or validations
- Maintained the original return values (including None where applicable)
