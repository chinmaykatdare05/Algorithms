def min_path_sum_recursive(grid, i, j):
    """
    Finds the minimum path sum using recursion.

    Time Complexity: O(2^(m+n)) (Exponential)
    Space Complexity: O(m+n) (Recursion depth)
    """
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return float("inf")  # Invalid position

    return grid[i][j] + min(
        min_path_sum_recursive(grid, i - 1, j),  # Move up
        min_path_sum_recursive(grid, i, j - 1),  # Move left
    )


# Example Usage
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m, n = len(grid), len(grid[0])
print(
    "Minimum Path Sum (Recursion):", min_path_sum_recursive(grid, m - 1, n - 1)
)  # Output: 7


def min_path_sum_dp(grid):
    """
    Finds the minimum path sum using Dynamic Programming.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Fill DP table
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]  # First row (only left movement)
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]  # First column (only top movement)
            else:
                dp[i][j] = grid[i][j] + min(
                    dp[i - 1][j], dp[i][j - 1]
                )  # Minimum of top & left

    return dp[m - 1][n - 1]


# Example Usage
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print("Minimum Path Sum (DP):", min_path_sum_dp(grid))  # Output: 7


def min_path_sum_space_optimized(grid):
    """
    Finds the minimum path sum using space-optimized DP.

    Time Complexity: O(m * n)
    Space Complexity: O(n) (Only one row stored)
    """
    m, n = len(grid), len(grid[0])
    dp = [float("inf")] * n

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[j] = grid[i][j]
            elif i == 0:
                dp[j] = dp[j - 1] + grid[i][j]  # First row
            elif j == 0:
                dp[j] = dp[j] + grid[i][j]  # First column
            else:
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])  # Minimum of top & left

    return dp[-1]


# Example Usage
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(
    "Minimum Path Sum (Space Optimized DP):", min_path_sum_space_optimized(grid)
)  # Output: 7
