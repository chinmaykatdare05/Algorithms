def bitwise_operations(a, b):
    """
    Demonstrates basic bitwise operations: AND, OR, XOR, NOT, Left Shift, Right Shift.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        dict: A dictionary containing results of all bitwise operations.

    Time Complexity: O(1) for each operation.
    Space Complexity: O(1)
    """
    results = {
        "AND": a & b,  # Bitwise AND
        "OR": a | b,  # Bitwise OR
        "XOR": a ^ b,  # Bitwise XOR
        "NOT a": ~a,  # Bitwise NOT (inverts bits, equivalent to -a-1)
        "NOT b": ~b,
        "a << 1": a << 1,  # Left shift (multiplies by 2)
        "b << 2": b << 2,
        "a >> 1": a >> 1,  # Right shift (divides by 2)
        "b >> 2": b >> 2,
    }

    return results


# 🎯 Example usage
a = 5  # Binary: 0101
b = 3  # Binary: 0011

results = bitwise_operations(a, b)
for operation, result in results.items():
    print(f"{operation}: {result}")

# ✅ Expected Output:
# AND: 1       (0101 & 0011 = 0001)
# OR: 7        (0101 | 0011 = 0111)
# XOR: 6       (0101 ^ 0011 = 0110)
# NOT a: -6    (~0101 = -(5+1))
# NOT b: -4    (~0011 = -(3+1))
# a << 1: 10   (5 * 2 = 10)
# b << 2: 12   (3 * 4 = 12)
# a >> 1: 2    (5 // 2 = 2)
# b >> 2: 0    (3 // 4 = 0)
