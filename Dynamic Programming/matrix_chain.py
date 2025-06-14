import sys


def matrix_chain_order(p):
    """
    Solves the Matrix Chain Multiplication problem using Dynamic Programming.

    Time Complexity: O(n^3) (where n is the number of matrices)
    Space Complexity: O(n^2) (for the DP table)

    Parameters:
        p (list): List of matrix dimensions, where matrix Ai has dimensions p[i-1] x p[i].

    Returns:
        int: Minimum number of scalar multiplications required.
    """
    n = len(p) - 1  # Number of matrices
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # L is the chain length (from 2 to n)
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):  # Matrices start index
            j = i + L - 1  # Matrices end index
            dp[i][j] = sys.maxsize

            # Try every possible partition point
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (p[i - 1] * p[k] * p[j])
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


# Example Usage
dimensions = [40, 20, 30, 10, 30]
print("Minimum Multiplications:", matrix_chain_order(dimensions))  # Output: 26000


import sys


def matrix_chain_order_with_parentheses(p):
    """
    Finds the minimum number of multiplications and prints the optimal parenthesization.

    Time Complexity: O(n^3)
    Space Complexity: O(n^2)

    Parameters:
        p (list): List of matrix dimensions.

    Returns:
        int: Minimum number of scalar multiplications required.
        str: Optimal parenthesization of matrices.
    """
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k  # Store partition point

    # Helper function to construct the parenthesization
    def construct_parenthesization(i, j):
        if i == j:
            return f"A{i}"
        k = split[i][j]
        left_part = construct_parenthesization(i, k)
        right_part = construct_parenthesization(k + 1, j)
        return f"({left_part} x {right_part})"

    return dp[1][n], construct_parenthesization(1, n)


# Example Usage
dimensions = [40, 20, 30, 10, 30]
min_cost, parenthesization = matrix_chain_order_with_parentheses(dimensions)
print("Minimum Multiplications:", min_cost)  # Output: 26000
print("Optimal Parenthesization:", parenthesization)  # Output: ((A1 x (A2 x A3)) x A4)
