import numpy as np


def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.

    Time Complexity: O(n^3) for n x n matrices.
    Space Complexity: O(n^2)

    Args:
        A (list[list[int]]): First matrix
        B (list[list[int]]): Second matrix

    Returns:
        list[list[int]]: Resultant matrix after multiplication.
    """
    return np.dot(A, B).tolist()


def matrix_exponentiation(matrix, exp):
    """
    Performs matrix exponentiation efficiently using exponentiation by squaring.

    Time Complexity: O(n^3 * log(exp))
    Space Complexity: O(n^2)

    Args:
        matrix (list[list[int]]): The matrix to exponentiate.
        exp (int): The exponent (non-negative integer).

    Returns:
        list[list[int]]: Matrix raised to the power of exp.
    """
    size = len(matrix)
    # Identity matrix of the same size
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # Exponentiation by squaring
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        exp //= 2

    return result


# 🎯 Example Usage: Fibonacci Numbers using Matrix Exponentiation
def fibonacci(n):
    """
    Calculates the nth Fibonacci number using matrix exponentiation.

    Time Complexity: O(log(n))
    Space Complexity: O(1)

    Args:
        n (int): The Fibonacci number to calculate.

    Returns:
        int: nth Fibonacci number.
    """
    if n <= 1:
        return n

    fib_matrix = [[1, 1], [1, 0]]

    result = matrix_exponentiation(fib_matrix, n - 1)
    return result[0][0]


# ✅ Test Cases
matrix = [[2, 1], [1, 1]]

exponent = 5
print("Matrix raised to power", exponent, ":", matrix_exponentiation(matrix, exponent))

print("Fibonacci(10):", fibonacci(10))
# Output: Fibonacci(10): 55
