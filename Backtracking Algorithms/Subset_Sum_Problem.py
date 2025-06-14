def subset_sum_recursive(nums, target, index=0):
    """
    Recursive Backtracking Solution for Subset Sum.

    Time Complexity: O(2^N)  (Exponential growth)
    Space Complexity: O(N)  (Recursive depth)
    """
    if target == 0:
        return True
    if index == len(nums) or target < 0:
        return False

    # Include current element or exclude it
    return subset_sum_recursive(
        nums, target - nums[index], index + 1
    ) or subset_sum_recursive(nums, target, index + 1)


# Example Usage
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum_recursive(nums, target))  # Output: True


def subset_sum_dp(nums, target):
    """
    Dynamic Programming (Bottom-Up) solution for Subset Sum.

    Time Complexity: O(N * S)  (Polynomial)
    Space Complexity: O(N * S)  (Can be optimized to O(S))
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum=0 can always be formed by an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] > j:  # Can't include this number
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target]


# Example Usage
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum_dp(nums, target))  # Output: True


def subset_sum_optimized(nums, target):
    """
    Space-Optimized DP Solution for Subset Sum.

    Time Complexity: O(N * S)
    Space Complexity: O(S)  (1D Array instead of 2D DP Table)
    """
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum=0 is always possible

    for num in nums:
        for j in range(target, num - 1, -1):  # Iterate backward to avoid overwriting
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# Example Usage
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum_optimized(nums, target))  # Output: True
