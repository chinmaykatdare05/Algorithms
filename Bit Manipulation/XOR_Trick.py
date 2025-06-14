def find_missing_number(arr):
    """
    Finds the missing number from an array of size n containing numbers from 1 to n+1 using XOR Trick.

    Args:
        arr (list): List of integers from 1 to n with one number missing.

    Returns:
        int: The missing number.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr) + 1

    # XOR of all numbers from 1 to n
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i

    # XOR of all numbers in the given array
    arr_xor = 0
    for num in arr:
        arr_xor ^= num

    # XOR of the two results gives the missing number
    return total_xor ^ arr_xor


# 🔥 Test Case
arr = [1, 2, 4, 5, 6]
print(f"Missing number: {find_missing_number(arr)}")

# ✅ Expected Output: Missing number: 3


def xor_swap(a, b):
    """
    Swaps two integers without using a temporary variable using XOR trick.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        tuple: Swapped integers (a, b).

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# 🔥 Test Case
a, b = 5, 7
a, b = xor_swap(a, b)
print(f"Swapped values: a = {a}, b = {b}")

# ✅ Expected Output: Swapped values: a = 7, b = 5
