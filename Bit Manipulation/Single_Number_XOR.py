def single_number(nums):
    """
    Finds the unique number in an array where all other elements appear twice.

    Args:
        nums (List[int]): The input array of integers.

    Returns:
        int: The unique number that appears only once.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    result = 0

    # XOR all numbers together
    for num in nums:
        result ^= num

    return result


# 🔥 Test Cases
print(single_number([4, 1, 2, 1, 2]))  # Expected Output: 4
print(single_number([2, 2, 3]))  # Expected Output: 3
print(single_number([7]))  # Expected Output: 7
