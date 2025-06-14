def pair_sum(nums, target):
    """
    Finds a pair of numbers that sum up to the target value.

    Time Complexity: O(n)
    - n: Number of elements in the nums list.
    - Each number is processed once.

    Space Complexity: O(n)
    - A set is used to store previously seen numbers.

    Args:
    nums (list): List of integers.
    target (int): The target sum.

    Returns:
    tuple: A pair of numbers that add up to the target (or None if no such pair exists).
    """
    seen = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            return (complement, num)

        seen.add(num)

    return None


# Test cases
nums = [2, 7, 11, 15]
target = 9
print("Pair:", pair_sum(nums, target))  # Output: (2, 7)

nums2 = [1, 5, 3, 8, 12]
target2 = 10
print("Pair:", pair_sum(nums2, target2))  # Output: (2, 8)

nums3 = [1, 2, 3, 4]
target3 = 100
print("Pair:", pair_sum(nums3, target3))  # Output: None
