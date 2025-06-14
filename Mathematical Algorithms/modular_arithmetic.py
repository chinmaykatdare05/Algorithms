def mod_add(a, b, mod):
    """
    Performs (a + b) % mod safely.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return (a % mod + b % mod) % mod


def mod_sub(a, b, mod):
    """
    Performs (a - b) % mod safely.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return (a % mod - b % mod + mod) % mod


def mod_mul(a, b, mod):
    """
    Performs (a * b) % mod efficiently.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return (a % mod * b % mod) % mod


def mod_exp(base, exp, mod):
    """
    Performs (base^exp) % mod using Exponentiation by Squaring (Fast Exponentiation).

    Time Complexity: O(log(exp))
    Space Complexity: O(1)

    This is useful for large powers with a modulus (e.g., cryptography).
    """
    result = 1
    base %= mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2

    return result


def mod_inv(a, mod):
    """
    Computes Modular Inverse using Extended Euclidean Algorithm.

    Time Complexity: O(log(mod))
    Space Complexity: O(1)

    Returns the modular inverse of 'a' under modulo 'mod',
    such that (a * mod_inv(a)) % mod == 1
    Works only when GCD(a, mod) == 1 (i.e., 'mod' is prime or 'a' is coprime with 'mod').
    """

    def extended_gcd(x, y):
        if y == 0:
            return x, 1, 0
        gcd, x1, y1 = extended_gcd(y, x % y)
        return gcd, y1, x1 - (x // y) * y1

    gcd, x, _ = extended_gcd(a, mod)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % mod


# 🎯 Example Usage
mod = 1000000007
a, b = 17, 23

print("Modular Addition:", mod_add(a, b, mod))  # Output: (17 + 23) % 1000000007 = 40
print(
    "Modular Subtraction:", mod_sub(a, b, mod)
)  # Output: (17 - 23) % 1000000007 = 999999997
print(
    "Modular Multiplication:", mod_mul(a, b, mod)
)  # Output: (17 * 23) % 1000000007 = 391
print("Modular Exponentiation:", mod_exp(a, b, mod))  # Output: (17^23) % 1000000007
print(
    "Modular Inverse of 17:", mod_inv(a, mod)
)  # Output: Modular inverse of 17 under 1000000007
