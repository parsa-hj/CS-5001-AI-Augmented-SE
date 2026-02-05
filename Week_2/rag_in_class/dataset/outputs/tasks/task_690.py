def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list."""
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
