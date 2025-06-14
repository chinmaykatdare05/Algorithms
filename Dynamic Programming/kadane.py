def max_subarray_sum(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    max_sum = float("-inf")  # Stores the maximum subarray sum
    current_sum = 0  # Tracks the current sum

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example Usage
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray_sum([1, 2, 3, -2, 5]))  # Output: 9
print(max_subarray_sum([-1, -2, -3, -4]))  # Output: -1


def max_subarray(nums):
    """
    Finds the maximum sum and the subarray using Kadane's Algorithm.

    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    max_sum = float("-inf")
    current_sum = 0
    start = end = temp_start = 0

    for i, num in enumerate(nums):
        if num > current_sum + num:
            current_sum = num
            temp_start = i  # New subarray starts
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i

    return max_sum, nums[start : end + 1]


# Example Usage
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Output: (6, [4, -1, 2, 1])
