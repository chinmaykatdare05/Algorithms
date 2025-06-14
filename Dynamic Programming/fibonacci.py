def fibonacci_recursive(n):
    """
    Computes the nth Fibonacci number using recursion.

    Time Complexity: O(2^n) (Exponential)
    Space Complexity: O(n) (Recursive stack)

    Parameters:
        n (int): Index of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Example usage
print("Fibonacci (Recursive):", fibonacci_recursive(10))  # Output: 55


def fibonacci_memoization(n, memo={}):
    """
    Computes the nth Fibonacci number using recursion with memoization.

    Time Complexity: O(n) (Linear)
    Space Complexity: O(n) (For memo dictionary)

    Parameters:
        n (int): Index of the Fibonacci number.
        memo (dict): Dictionary to store computed values.

    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# Example usage
print("Fibonacci (Memoization):", fibonacci_memoization(10))  # Output: 55


def fibonacci_iterative(n):
    """
    Computes the nth Fibonacci number using iteration.

    Time Complexity: O(n) (Linear)
    Space Complexity: O(1) (Constant)

    Parameters:
        n (int): Index of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Example usage
print("Fibonacci (Iterative):", fibonacci_iterative(10))  # Output: 55


def fibonacci_matrix(n):
    """
    Computes the nth Fibonacci number using Matrix Exponentiation.

    Time Complexity: O(log n) (Efficient)
    Space Complexity: O(1) (Constant)

    Parameters:
        n (int): Index of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """

    def matrix_mult(A, B):
        return [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ],
        ]

    def matrix_exponentiation(M, exp):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while exp:
            if exp % 2:
                result = matrix_mult(result, M)
            M = matrix_mult(M, M)
            exp //= 2
        return result

    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_exponentiation(F, n - 1)
    return result[0][0]


# Example usage
print("Fibonacci (Matrix Exponentiation):", fibonacci_matrix(10))  # Output: 55


import math


def fibonacci_binet(n):
    """
    Computes the nth Fibonacci number using Binet's Formula.

    Time Complexity: O(1) (Constant)
    Space Complexity: O(1) (Constant)

    Parameters:
        n (int): Index of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number (rounded to the nearest integer).
    """
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))


# Example usage
print("Fibonacci (Binet's Formula):", fibonacci_binet(10))  # Output: 55
