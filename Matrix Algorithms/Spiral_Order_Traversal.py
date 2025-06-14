def spiral_order(matrix):
    """
    Returns the elements of a matrix in spiral order.

    Time Complexity: O(m * n)
    - Each element is visited once.

    Space Complexity: O(m * n)
    - The output list stores all matrix elements.

    Args:
        matrix (list of lists): A 2D matrix with m rows and n columns.

    Returns:
        list: A list containing elements in spiral order.
    """
    result = []

    if not matrix:
        return result

    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left (if rows remain)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from bottom to top (if columns remain)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# Test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix:")
for row in matrix:
    print(row)

spiral_result = spiral_order(matrix)

print("\nSpiral Order Traversal:")
print(spiral_result)
