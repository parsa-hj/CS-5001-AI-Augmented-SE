# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if (abs(left_height - right_height) <= 1) and is_tree_balanced(root.left) and is_tree_balanced(root.right):
        return True
    return False
```

- Preserved all function names, argument lists, and return types exactly as in the original
- Maintained the exact same logic for height calculation and balance checking
- Kept the recursive structure and control flow identical to the original
- Ensured all edge cases (None root, single node, etc.) behave the same way
- Used the same comparison operators and conditions as the original implementation
- Preserved the exact same return values (True/False/None) for all cases
- Maintained the same algorithmic approach without any optimizations that could alter behavior
