from collections import defaultdict


def longest_arith_seq_length(nums):
    """
    Finds the length of the longest arithmetic subsequence using DP with HashMap.

    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    max_length = 1

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]  # Calculate common difference
            dp[i][diff] = dp[j][diff] + 1 if diff in dp[j] else 2
            max_length = max(max_length, dp[i][diff])

    return max_length


# Example Usage
print(longest_arith_seq_length([3, 6, 9, 12]))  # Output: 4
print(longest_arith_seq_length([9, 4, 7, 2, 10]))  # Output: 3
print(longest_arith_seq_length([20, 1, 15, 3, 10, 5, 8]))  # Output: 4
