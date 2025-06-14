def count_set_bits(n):
    """
    Counts the number of set bits (1s) in the binary representation of a number
    using Brian Kernighan's Algorithm.

    Args:
        n (int): The input number.

    Returns:
        int: The count of set bits in the number.

    Time Complexity: O(k), where k is the number of set bits.
    Space Complexity: O(1)
    """
    count = 0
    while n:
        n &= n - 1  # Flip the last set bit to 0
        count += 1
    return count


# 🎯 Example usage
numbers = [5, 9, 15, 23, 255]

for num in numbers:
    print(f"Number: {num}, Set Bits: {count_set_bits(num)}")

# ✅ Expected Output:
# Number: 5, Set Bits: 2    (5 = 101)
# Number: 9, Set Bits: 2    (9 = 1001)
# Number: 15, Set Bits: 4   (15 = 1111)
# Number: 23, Set Bits: 4   (23 = 10111)
# Number: 255, Set Bits: 8  (255 = 11111111)


def count_set_bits_builtin(n):
    return bin(n).count("1")
