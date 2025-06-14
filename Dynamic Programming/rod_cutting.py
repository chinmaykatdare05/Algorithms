def rod_cutting_recursive(prices, n):
    """
    Solves the rod cutting problem using recursion.

    Time Complexity: O(2^n) (Exponential)
    Space Complexity: O(n) (Recursion depth)
    """
    if n == 0:
        return 0

    max_profit = float("-inf")
    for i in range(n):
        profit = prices[i] + rod_cutting_recursive(prices, n - (i + 1))
        max_profit = max(max_profit, profit)

    return max_profit


# Example Usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = len(prices)
print(
    "Maximum Profit (Recursion):", rod_cutting_recursive(prices, rod_length)
)  # Output: 22


def rod_cutting_dp(prices, n):
    """
    Solves the rod cutting problem using Dynamic Programming.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    dp = [0] * (n + 1)

    for length in range(1, n + 1):
        max_profit = float("-inf")
        for cut in range(length):
            max_profit = max(max_profit, prices[cut] + dp[length - cut - 1])
        dp[length] = max_profit

    return dp[n]


# Example Usage
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = len(prices)
print("Maximum Profit (DP):", rod_cutting_dp(prices, rod_length))  # Output: 22
