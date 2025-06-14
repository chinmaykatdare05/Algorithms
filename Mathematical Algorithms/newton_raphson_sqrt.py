def newton_raphson_sqrt(n, epsilon=1e-6):
    """
    Computes the square root of a number using the Newton-Raphson method.

    Args:
        n (float): The number to find the square root of.
        epsilon (float): The error tolerance (default is 1e-6).

    Returns:
        float: The approximate square root of the number.

    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number!")

    # Edge cases
    if n == 0 or n == 1:
        return n

    # Initial guess (can start with n/2 or any reasonable number)
    guess = n / 2.0

    # Iteratively improve the guess using Newton-Raphson formula
    while abs(guess * guess - n) > epsilon:
        guess = 0.5 * (guess + n / guess)

    return guess


# 🎯 Example usage
num = 25
result = newton_raphson_sqrt(num)
print(f"Square root of {num} ≈ {result:.6f}")
# Output: Square root of 25 ≈ 5.000000

num = 0.01
result = newton_raphson_sqrt(num)
print(f"Square root of {num} ≈ {result:.6f}")
# Output: Square root of 0.01 ≈ 0.100000
