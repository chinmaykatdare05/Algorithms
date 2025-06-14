def min_coins(coins, V):
    """
    Finds the minimum number of coins required to make amount V.

    Time Complexity: O(V * n) (where V is the amount and n is the number of coins)
    Space Complexity: O(V)

    Parameters:
        coins (list): List of coin denominations.
        V (int): Target value.

    Returns:
        int: Minimum number of coins required to make V, or -1 if impossible.
    """
    dp = [float("inf")] * (V + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for i in range(1, V + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[V] if dp[V] != float("inf") else -1  # Return -1 if impossible


# Example Usage
coins = [1, 3, 4]
V = 6
print("Minimum Coins Required:", min_coins(coins, V))  # Output: 2 (3+3 or 4+1+1)


def coin_change_ways(coins, V):
    """
    Finds the total number of ways to make amount V using given coin denominations.

    Time Complexity: O(V * n) (where V is the amount and n is the number of coins)
    Space Complexity: O(V)

    Parameters:
        coins (list): List of coin denominations.
        V (int): Target value.

    Returns:
        int: Number of ways to make V.
    """
    dp = [0] * (V + 1)
    dp[0] = 1  # Base case: 1 way to make 0 (choosing no coins)

    for coin in coins:
        for i in range(coin, V + 1):
            dp[i] += dp[i - coin]

    return dp[V]


# Example Usage
coins = [1, 2, 3]
V = 4
print("Total Ways to Make", V, ":", coin_change_ways(coins, V))  # Output: 4
