def tiling_ways(n):
    """
    Returns the number of ways to tile a 2xN board with 2x1 tiles.

    Args:
    n (int): Size of the board (2 x n).

    Returns:
    int: Number of ways to tile the board.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Iterative approach (bottom-up DP)
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


# Example usage:
n = 5
print(f"Number of ways to tile 2x{n} board:", tiling_ways(n))
