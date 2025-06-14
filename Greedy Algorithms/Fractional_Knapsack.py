def fractional_knapsack(items, W):
    """
    Solves the Fractional Knapsack Problem using a greedy approach.

    Time Complexity: O(N log N)  (Sorting items by value/weight ratio)
    Space Complexity: O(1)
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0  # Maximum value we can carry
    for value, weight in items:
        if W >= weight:  # If we can take the whole item
            W -= weight
            total_value += value
        else:  # If we can only take a fraction
            total_value += value * (W / weight)
            break  # Knapsack is full

    return total_value


# Example Usage
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
print(fractional_knapsack(items, capacity))  # Output: 240.0
