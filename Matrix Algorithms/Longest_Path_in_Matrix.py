def find_longest_path(matrix):
    """
    Finds the longest increasing path in a matrix.

    Time Complexity: O(m * n)
    - Each cell is visited once and cached for quick retrieval.

    Space Complexity: O(m * n)
    - Due to the memoization table and recursion stack.

    Args:
        matrix (list of lists): A 2D matrix of integers.

    Returns:
        int: Length of the longest increasing path.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    # Memoization table to store longest path from each cell
    memo = [[-1] * cols for _ in range(rows)]

    # Directions for moving: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c, prev_value):
        # Base case: if out of bounds or value is not increasing
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_value:
            return 0

        # If already computed, return memoized result
        if memo[r][c] != -1:
            return memo[r][c]

        max_path = 0
        for dr, dc in directions:
            max_path = max(max_path, dfs(r + dr, c + dc, matrix[r][c]))

        # Include current cell in the path length
        memo[r][c] = 1 + max_path
        return memo[r][c]

    # Start from each cell and find the maximum path
    longest_path = 0
    for r in range(rows):
        for c in range(cols):
            longest_path = max(longest_path, dfs(r, c, -1))

    return longest_path


# Test case
matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

print("Longest Increasing Path Length:", find_longest_path(matrix))
