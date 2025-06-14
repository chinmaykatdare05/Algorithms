def rotate_matrix(matrix):
    """
    Rotates a square matrix 90 degrees clockwise in-place.

    Time Complexity: O(n²)
    - Each element is moved once.

    Space Complexity: O(1)
    - Rotates in-place without extra memory.

    Args:
        matrix (list of lists): A square matrix (n x n).

    Returns:
        None: Modifies the matrix in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


# Test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix:")
for row in matrix:
    print(row)

rotate_matrix(matrix)

print("\nRotated Matrix (90 degrees clockwise):")
for row in matrix:
    print(row)
