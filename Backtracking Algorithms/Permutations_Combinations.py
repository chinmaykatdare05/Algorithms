from itertools import permutations, combinations, combinations_with_replacement


def generate_permutations(elements, r=None):
    """
    Generates all possible permutations of given elements.

    Time Complexity: O(n!) for full permutations, O(nPr) for partial.
    Space Complexity: O(n!) as all permutations are stored in memory.

    Args:
        elements (list): List of elements to permute.
        r (int, optional): Length of permutation. Defaults to full length.

    Returns:
        list: List of permutations.
    """
    return list(permutations(elements, r))


def generate_combinations(elements, r):
    """
    Generates all possible combinations of given elements.

    Time Complexity: O(nCr) = O(n! / (r! * (n-r)!))
    Space Complexity: O(nCr) as all combinations are stored.

    Args:
        elements (list): List of elements to choose from.
        r (int): Length of combination.

    Returns:
        list: List of combinations.
    """
    return list(combinations(elements, r))


def generate_combinations_with_replacement(elements, r):
    """
    Generates combinations with replacement (allows repeated elements).

    Time Complexity: O((n+r-1)! / (r! * (n-1)!))
    Space Complexity: O(nCr) as all combinations are stored.

    Args:
        elements (list): List of elements.
        r (int): Length of combination.

    Returns:
        list: List of combinations with replacement.
    """
    return list(combinations_with_replacement(elements, r))


# Example Usage
elements = ["A", "B", "C"]
r = 2

print("Permutations:", generate_permutations(elements, r))
print("Combinations:", generate_combinations(elements, r))
print(
    "Combinations with Replacement:",
    generate_combinations_with_replacement(elements, r),
)


import math


def permutation(n, r):
    """
    Calculates P(n, r) = n! / (n-r)!

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        n (int): Total items.
        r (int): Items to arrange.

    Returns:
        int: Number of permutations.
    """
    return math.factorial(n) // math.factorial(n - r)


def combination(n, r):
    """
    Calculates C(n, r) = n! / (r! * (n-r)!)

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        n (int): Total items.
        r (int): Items to choose.

    Returns:
        int: Number of combinations.
    """
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


# Example Usage
n, r = 5, 3
print("Permutation P(5,3):", permutation(n, r))
print("Combination C(5,3):", combination(n, r))
