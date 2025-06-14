def gcd(a, b):
    """
    Helper function to compute the Greatest Common Divisor (GCD) using the Euclidean Algorithm.
    """
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """
    Computes the Least Common Multiple (LCM) of two integers using the relationship:
    LCM(a, b) = abs(a * b) / GCD(a, b)

    Time Complexity: O(log(min(a, b)))
    - GCD is the dominant operation, which runs in logarithmic time.

    Space Complexity: O(1)
    - Only a few variables are used.

    :param a: int - First integer
    :param b: int - Second integer
    :return: int - The LCM of a and b
    """
    if a == 0 or b == 0:
        return 0  # LCM of zero with any number is zero
    return abs(a * b) // gcd(a, b)


# 🎯 Example Usage
print("LCM of 12 and 15:", lcm(12, 15))  # Output: 60
print("LCM of 7 and 5:", lcm(7, 5))  # Output: 35
