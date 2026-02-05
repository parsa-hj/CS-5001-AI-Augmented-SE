def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements in lst1 and lst2."""
    result = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return result
