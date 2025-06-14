import numpy as np


def add_matrix(A, B):
    """Performs matrix addition."""
    return np.add(A, B)


def subtract_matrix(A, B):
    """Performs matrix subtraction."""
    return np.subtract(A, B)


def strassen_multiplication(A, B):
    """
    Multiplies two matrices using Strassen's Algorithm.

    Time Complexity:
        - Best/Average/Worst Case: O(N^log7) ≈ O(N^2.81)

    Space Complexity: O(N^2) (Extra storage for submatrices)

    Args:
        A (np.ndarray): First square matrix.
        B (np.ndarray): Second square matrix.

    Returns:
        np.ndarray: The result of multiplying A and B.
    """
    n = len(A)

    # Base case: 1x1 matrix multiplication
    if n == 1:
        return A * B

    # Splitting matrices into quadrants
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # Compute the 7 matrices using Strassen's formulas
    M1 = strassen_multiplication(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_multiplication(add_matrix(A21, A22), B11)
    M3 = strassen_multiplication(A11, subtract_matrix(B12, B22))
    M4 = strassen_multiplication(A22, subtract_matrix(B21, B11))
    M5 = strassen_multiplication(add_matrix(A11, A12), B22)
    M6 = strassen_multiplication(subtract_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_multiplication(subtract_matrix(A12, A22), add_matrix(B21, B22))

    # Compute the final quadrants of the result matrix
    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(subtract_matrix(add_matrix(M1, M3), M2), M6)

    # Combine submatrices into the final matrix
    C = np.zeros((n, n))
    C[:mid, :mid], C[:mid, mid:] = C11, C12
    C[mid:, :mid], C[mid:, mid:] = C21, C22

    return C


# Example Usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = strassen_multiplication(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Strassen Multiplication Result:\n", result)
