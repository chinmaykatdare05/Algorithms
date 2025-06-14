import math


def find_msb(n):
    """
    Finds the position of the Most Significant Bit (MSB) in the binary representation of a number.

    Args:
        n (int): The input number.

    Returns:
        int: The position of the MSB (0-based).

    Time Complexity: O(1) using logarithm.
    Space Complexity: O(1)
    """
    if n == 0:
        return -1  # Edge case: No MSB for 0

    # Method 1: Using logarithm (base 2)
    return int(math.log2(n))


# 🎯 Example usage
numbers = [18, 32, 77, 128, 255]

for num in numbers:
    print(f"Number: {num}, MSB Position: {find_msb(num)}")

# ✅ Expected Output:
# Number: 18, MSB Position: 4    (18 = 10010, MSB at index 4)
# Number: 32, MSB Position: 5    (32 = 100000, MSB at index 5)
# Number: 77, MSB Position: 6    (77 = 1001101, MSB at index 6)
# Number: 128, MSB Position: 7   (128 = 10000000, MSB at index 7)
# Number: 255, MSB Position: 7   (255 = 11111111, MSB at index 7)


def find_msb_bitshift(n):
    """
    Bitwise approach to find the Most Significant Bit (MSB).
    """
    if n == 0:
        return -1

    msb = 0
    while n > 1:
        n >>= 1
        msb += 1

    return msb


# ✅ Output is identical to the previous version
