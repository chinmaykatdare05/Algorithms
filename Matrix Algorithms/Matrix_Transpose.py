def transpose_matrix(matrix):
    """
    Transposes the given matrix.

    Time Complexity: O(m * n)
    - m is the number of rows, n is the number of columns.
    - Each element is accessed once.

    Space Complexity: O(n * m)
    - A new matrix of swapped dimensions is created.

    Args:
        matrix (list of lists): A 2D matrix (m x n).

    Returns:
        list of lists: The transposed matrix (n x m).
    """

    # Using list comprehension to swap rows and columns
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix:")
for row in matrix:
    print(row)

transposed = transpose_matrix(matrix)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
