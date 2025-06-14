def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.

    Time Complexity: O(n * W) (where n = number of items, W = knapsack capacity)
    Space Complexity: O(n * W) (for DP table)

    Parameters:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (int): Maximum weight the knapsack can hold.

    Returns:
        int: Maximum total value that can be obtained.
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # Can take this item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:  # Cannot take this item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(
    "0/1 Knapsack Maximum Value:", knapsack_01(weights, values, capacity)
)  # Output: 7


def fractional_knapsack(weights, values, capacity):
    """
    Solves the Fractional Knapsack problem using a Greedy approach.

    Time Complexity: O(n log n) (Sorting items by value-to-weight ratio)
    Space Complexity: O(1)

    Parameters:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (int): Maximum weight the knapsack can hold.

    Returns:
        float: Maximum total value that can be obtained.
    """
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])  # Sort by value/weight ratio

    total_value = 0.0
    for ratio, weight, value in items:
        if capacity >= weight:  # Take full item
            total_value += value
            capacity -= weight
        else:  # Take fraction of item
            total_value += ratio * capacity
            break

    return total_value


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(
    "Fractional Knapsack Maximum Value:", fractional_knapsack(weights, values, capacity)
)  # Output: 240.0
