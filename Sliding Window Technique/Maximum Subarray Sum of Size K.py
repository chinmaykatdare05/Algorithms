def max_subarray_sum_k(nums, k):
    """
    Finds the maximum sum of any subarray with size K.

    Args:
        nums (List[int]): The input array of integers.
        k (int): Size of the subarray.

    Returns:
        int: The maximum sum of any subarray of size K.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Edge case: if the array is smaller than k
    if len(nums) < k:
        return -1

    # Calculate the sum of the first window of size k
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window through the array
    for i in range(k, len(nums)):
        # Slide the window: remove the left element, add the new right element
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# 🔥 Test Cases
print(max_subarray_sum_k([2, 1, 5, 1, 3, 2], 3))  # Expected Output: 9 (5+1+3)
print(max_subarray_sum_k([1, 2, 3, 4, 5], 2))  # Expected Output: 9 (4+5)
print(max_subarray_sum_k([3, -1, 4, 12, -8, 5, 6], 4))  # Expected Output: 18 (4+12-8+5)
