import math


def prime_factorization(n):
    """
    Finds the prime factorization of a number n.

    Time Complexity: O(sqrt(n))
    Space Complexity: O(log(n)) — storing factors.

    Args:
        n (int): The number to factorize (n > 0).

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []

    # Count the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd numbers from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still a prime number > 2
    if n > 2:
        factors.append(n)

    return factors


# 🎯 Example Usage
num = 315
print(f"Prime factors of {num}: {prime_factorization(num)}")
# Output: Prime factors of 315: [3, 3, 5, 7]
