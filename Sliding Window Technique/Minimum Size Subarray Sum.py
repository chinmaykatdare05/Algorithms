def min_size_subarray_sum(target, nums):
    """
    Finds the smallest contiguous subarray with a sum >= target.

    Args:
        target (int): The target sum to achieve.
        nums (List[int]): The input array of positive integers.

    Returns:
        int: Length of the smallest subarray with sum >= target.
        Returns 0 if no such subarray exists.

    Time Complexity: O(n)
    Space Complexity: O(1) — only a few variables are maintained.
    """

    # Initialize sliding window pointers and sum tracker
    left = 0
    current_sum = 0
    min_length = float("inf")  # Start with a large number

    # Expand the window by moving 'right'
    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window from the left while the sum is ≥ target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    # Return the minimum length found, or 0 if no valid subarray exists
    return min_length if min_length != float("inf") else 0


# 🔥 Test Cases
print(min_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]))  # Expected Output: 2 ([4,3])
print(min_size_subarray_sum(11, [1, 2, 3, 4, 5]))  # Expected Output: 3 ([3,4,5])
print(min_size_subarray_sum(100, [1, 2, 3]))  # Expected Output: 0 (No subarray found)
