def subset_sum(nums, target):
    """
    Determines if there exists a subset with the given sum using DP.

    Time Complexity: O(N × S)
    Space Complexity: O(N × S)
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base Case: Sum 0 is always possible with an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


# Example Usage
print(subset_sum([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(subset_sum([3, 34, 4, 12, 5, 2], 30))  # Output: False


def subset_sum_optimized(nums, target):
    """
    Space-optimized DP solution for the subset sum problem.

    Time Complexity: O(N × S)
    Space Complexity: O(S)
    """
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum 0 is always possible

    # Process elements one by one
    for num in nums:
        for j in range(target, num - 1, -1):  # Traverse backwards
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# Example Usage
print(subset_sum_optimized([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(subset_sum_optimized([3, 34, 4, 12, 5, 2], 30))  # Output: False


def subset_sum_recursive(nums, target, index=0):
    """
    Recursive approach for subset sum problem.

    Time Complexity: O(2^N)
    Space Complexity: O(N) (recursion depth)
    """
    if target == 0:
        return True
    if index >= len(nums) or target < 0:
        return False

    # Include or exclude the current element
    return subset_sum_recursive(
        nums, target - nums[index], index + 1
    ) or subset_sum_recursive(nums, target, index + 1)


# Example Usage
print(subset_sum_recursive([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(subset_sum_recursive([3, 34, 4, 12, 5, 2], 30))  # Output: False
