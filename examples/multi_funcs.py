def is_even(n):
    """Return True if n is even, else False."""
    if not isinstance(n, int):
        return False
    return n % 2 == 0


def reverse_string(s):
    """Return the reversed version of the input string."""
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]


def sum_list(nums):
    """Return the sum of a list of numbers."""
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements must be numbers")
    return sum(nums)
