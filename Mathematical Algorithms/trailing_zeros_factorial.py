def count_trailing_zeros(n):
    """
    Counts the number of trailing zeros in n! (n factorial).

    Time Complexity: O(log(n))
    Space Complexity: O(1)

    Args:
        n (int): The number whose factorial's trailing zeros are to be counted.

    Returns:
        int: The count of trailing zeros in n!.
    """
    count = 0
    # Count the number of 5s in the prime factorization of n!
    while n >= 5:
        n //= 5
        count += n

    return count


# 🎯 Example Usage
num = 100
print(f"Trailing zeros in {num}!: {count_trailing_zeros(num)}")
# Output: Trailing zeros in 100!: 24
