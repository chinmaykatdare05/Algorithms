def gcd(a, b):
    """
    Computes the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.

    Time Complexity: O(log(min(a, b)))
    - Each step reduces the problem size roughly by half.

    Space Complexity: O(1)
    - Only a few variables are used.

    :param a: int - First integer
    :param b: int - Second integer
    :return: int - The GCD of a and b
    """
    while b:
        a, b = b, a % b  # Keep reducing a and b until b becomes 0
    return abs(a)


# 🎯 Example Usage
print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6
print("GCD of 101 and 103:", gcd(101, 103))  # Output: 1 (they are co-prime)
