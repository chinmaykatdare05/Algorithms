import math


def is_power_of_two(n):
    """
    Checks if a number is a power of two using bit manipulation.

    A number is a power of two if it has only one set bit in its binary representation.
    For example:
    - 1 -> 0001 (2^0)
    - 2 -> 0010 (2^1)
    - 4 -> 0100 (2^2)
    - 8 -> 1000 (2^3)

    Key Insight:
    A power of two has only one '1' bit, so n & (n - 1) should be 0.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a power of two, False otherwise.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0


# 🎯 Example usage
numbers = [1, 2, 3, 4, 8, 16, 31, 64, 127, 128]

for num in numbers:
    print(f"Number: {num}, Is Power of Two? {is_power_of_two(num)}")

# ✅ Expected Output:
# Number: 1, Is Power of Two? True
# Number: 2, Is Power of Two? True
# Number: 3, Is Power of Two? False
# Number: 4, Is Power of Two? True
# Number: 8, Is Power of Two? True
# Number: 16, Is Power of Two? True
# Number: 31, Is Power of Two? False
# Number: 64, Is Power of Two? True
# Number: 127, Is Power of Two? False
# Number: 128, Is Power of Two? True


def is_power_of_two_log(n):
    return n > 0 and math.log2(n).is_integer()
