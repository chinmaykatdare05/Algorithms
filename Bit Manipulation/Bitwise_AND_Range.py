def range_bitwise_and(left, right):
    """
    Performs bitwise AND on all integers between left and right (inclusive).

    Args:
        left (int): The start of the range.
        right (int): The end of the range.

    Returns:
        int: Result of bitwise AND from left to right.

    Time Complexity: O(log(right))
    Space Complexity: O(1)
    """
    shift = 0

    # Keep shifting left and right to the right until they are equal
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    # Shift the common prefix back to the left
    return left << shift


# 🔥 Test Cases
print(range_bitwise_and(5, 7))  # Expected Output: 4
print(range_bitwise_and(0, 1))  # Expected Output: 0
print(range_bitwise_and(12, 15))  # Expected Output: 12
