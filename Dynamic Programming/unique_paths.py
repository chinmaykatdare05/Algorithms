def unique_paths_recursive(m, n):
    """
    Finds the number of unique paths using recursion.

    Time Complexity: O(2^(m+n)) (Exponential)
    Space Complexity: O(m+n) (Recursion depth)
    """

    def count_paths(i, j):
        if i == m - 1 or j == n - 1:
            return 1  # Only one way to go
        return count_paths(i + 1, j) + count_paths(i, j + 1)

    return count_paths(0, 0)


# Example Usage
print("Unique Paths (Recursion):", unique_paths_recursive(3, 7))  # Output: 28


def unique_paths_dp(m, n):
    """
    Finds the number of unique paths using Dynamic Programming.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    dp = [[1] * n for _ in range(m)]  # Initialize first row & column as 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# Example Usage
print("Unique Paths (DP):", unique_paths_dp(3, 7))  # Output: 28


def unique_paths_space_optimized(m, n):
    """
    Finds the number of unique paths using space-optimized DP.

    Time Complexity: O(m * n)
    Space Complexity: O(n) (Only one row stored)
    """
    prev_row = [1] * n  # Initialize first row as 1

    for i in range(1, m):
        new_row = [1] * n
        for j in range(1, n):
            new_row[j] = new_row[j - 1] + prev_row[j]
        prev_row = new_row  # Move to the next row

    return prev_row[-1]


# Example Usage
print(
    "Unique Paths (Space Optimized DP):", unique_paths_space_optimized(3, 7)
)  # Output: 28


import math


def unique_paths_combinatorics(m, n):
    """
    Finds the number of unique paths using Combinatorics.

    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    return math.comb(m + n - 2, m - 1)  # Binomial Coefficient


# Example Usage
print("Unique Paths (Combinatorics):", unique_paths_combinatorics(3, 7))  # Output: 28
