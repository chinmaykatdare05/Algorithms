def fast_exponentiation(base, exp):
    """
    Computes base^exp using Exponentiation by Squaring (Recursive Method).

    Time Complexity: O(log(exp))
    Space Complexity: O(log(exp)) — due to recursion stack.

    Args:
        base (int): The base number.
        exp (int): The exponent (non-negative integer).

    Returns:
        int: The result of base^exp.
    """
    if exp == 0:
        return 1
    half = fast_exponentiation(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base


def fast_exponentiation_iterative(base, exp):
    """
    Computes base^exp using Exponentiation by Squaring (Iterative Method).

    Time Complexity: O(log(exp))
    Space Complexity: O(1)

    Args:
        base (int): The base number.
        exp (int): The exponent (non-negative integer).

    Returns:
        int: The result of base^exp.
    """
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result


# 🎯 Example Usage
base = 3
exp = 13

print("Recursive Fast Exponentiation:", fast_exponentiation(base, exp))
# Output: 1594323 (3^13)

print("Iterative Fast Exponentiation:", fast_exponentiation_iterative(base, exp))
# Output: 1594323 (3^13)
