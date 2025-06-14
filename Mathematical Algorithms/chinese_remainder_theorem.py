from functools import reduce


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find gcd and modular inverse.
    Returns gcd(a, b), x, y such that a*x + b*y = gcd(a, b).

    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, m):
    """
    Returns the modular inverse of 'a' under modulo 'm'.
    Uses Extended Euclidean Algorithm.

    Time Complexity: O(log(m))
    Space Complexity: O(1)
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse does not exist")
    return x % m


def chinese_remainder_theorem(nums, rems):
    """
    Solves a system of congruences using the Chinese Remainder Theorem (CRT).

    Given:
    x ≡ rems[0] (mod nums[0])
    x ≡ rems[1] (mod nums[1])
    ...
    x ≡ rems[k-1] (mod nums[k-1])

    Time Complexity: O(n * log(M)), where n = len(nums), M = product of all moduli
    Space Complexity: O(1)

    Args:
        nums (list[int]): List of moduli.
        rems (list[int]): List of corresponding remainders.

    Returns:
        int: Smallest solution 'x' satisfying all the equations.
    """
    if len(nums) != len(rems):
        raise ValueError("Number of moduli and remainders must match!")

    # Compute product of all moduli
    product = reduce(lambda a, b: a * b, nums)
    result = 0

    # Apply the formula: x = Σ (rems[i] * partial_product * modular_inverse)
    for n_i, a_i in zip(nums, rems):
        partial_product = product // n_i
        inverse = mod_inverse(partial_product, n_i)
        result += a_i * partial_product * inverse

    return result % product


# 🎯 Example Usage
nums = [3, 5, 7]
rems = [2, 3, 2]
result = chinese_remainder_theorem(nums, rems)
print(
    f"Solution for the given congruences: x ≡ {result} (mod {reduce(lambda a, b: a * b, nums)})"
)
# Output: Solution for the given congruences: x ≡ 23 (mod 105)
