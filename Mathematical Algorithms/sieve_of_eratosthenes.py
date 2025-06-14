def sieve_of_eratosthenes(n):
    """
    Generates all prime numbers up to 'n' using the Sieve of Eratosthenes algorithm.

    Time Complexity: O(n log(log n))
    - The inner loop skips multiples in an optimized way, leading to this near-linear performance.

    Space Complexity: O(n)
    - We maintain a boolean array of size 'n+1' to track prime numbers.

    :param n: int - The upper limit to generate prime numbers.
    :return: list[int] - A list of all prime numbers up to 'n'.
    """
    if n < 2:
        return []

    # Step 1: Initialize a boolean list assuming all numbers are prime
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

    # Step 2: Mark non-primes by crossing out multiples of each prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Step 3: Collect all the numbers still marked as prime
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes


# 🎯 Example Usage
n = 50
print(f"Prime numbers up to {n}:", sieve_of_eratosthenes(n))
