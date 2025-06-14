def max_product_subarray(nums):
    """
    Finds the maximum product subarray in a given integer array.

    Args:
        nums (List[int]): The input array of integers.

    Returns:
        int: Maximum product of any contiguous subarray.

    Time Complexity: O(n)
    Space Complexity: O(1) — we only track a few variables, no extra data structures.
    """

    # Edge case: empty array
    if not nums:
        return 0

    # Initialize variables
    max_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    # Traverse the array from the second element onward
    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swap max and min
        if num < 0:
            current_max, current_min = current_min, current_max

        # Update current max and min product at this index
        current_max = max(num, num * current_max)
        current_min = min(num, num * current_min)

        # Track the global maximum product
        max_product = max(max_product, current_max)

    return max_product


# 🔥 Test Cases
print(max_product_subarray([2, 3, -2, 4]))  # Expected Output: 6 ([2, 3])
print(max_product_subarray([-2, 0, -1]))  # Expected Output: 0 ([0])
print(max_product_subarray([-1, -3, -10, 0, 60]))  # Expected Output: 60 ([60])
print(max_product_subarray([1, 2, 3, 4]))  # Expected Output: 24 ([1, 2, 3, 4])
