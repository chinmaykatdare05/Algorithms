def egg_dropping(k, n):
    """
    Determines the minimum number of attempts needed to find the critical floor.

    Time Complexity: O(K * N^2)
    Space Complexity: O(K * N)
    """
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base Cases
    for i in range(1, k + 1):
        dp[i][0] = 0  # 0 floors require 0 trials
        dp[i][1] = 1  # 1 floor requires 1 trial
    for j in range(1, n + 1):
        dp[1][j] = j  # With 1 egg, try all floors one by one

    # Fill DP table
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float("inf")
            for x in range(1, j + 1):
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                dp[i][j] = min(dp[i][j], res)

    return dp[k][n]


# Example Usage
print(egg_dropping(2, 10))  # Output: 4
print(egg_dropping(3, 14))  # Output: 4


def egg_dropping_optimized(k, n):
    """
    Optimized approach using Binary Search and DP.

    Time Complexity: O(K * N log N)
    Space Complexity: O(K * N)
    """
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Base Cases
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    for j in range(1, n + 1):
        dp[1][j] = j

    # Fill DP table using binary search
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            low, high, result = 1, j, float("inf")
            while low <= high:
                mid = (low + high) // 2
                break_case = dp[i - 1][mid - 1]  # Egg breaks
                no_break_case = dp[i][j - mid]  # Egg doesn't break
                worst_case = 1 + max(break_case, no_break_case)

                if break_case > no_break_case:
                    high = mid - 1  # Move down
                else:
                    low = mid + 1  # Move up

                result = min(result, worst_case)

            dp[i][j] = result

    return dp[k][n]


# Example Usage
print(egg_dropping_optimized(2, 10))  # Output: 4
print(egg_dropping_optimized(3, 14))  # Output: 4


def super_egg_drop(k, n):
    """
    Optimized approach using Mathematical DP.

    Time Complexity: O(K log N)
    Space Complexity: O(K)
    """
    dp = [0] * (k + 1)
    moves = 0

    while dp[k] < n:
        moves += 1
        for i in range(k, 0, -1):
            dp[i] = dp[i - 1] + dp[i] + 1

    return moves


# Example Usage
print(super_egg_drop(2, 10))  # Output: 4
print(super_egg_drop(3, 14))  # Output: 4
