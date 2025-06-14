def is_palindrome(s, i, j):
    return s[i : j + 1] == s[i : j + 1][::-1]


def min_partitions_recursive(s, i, j):
    """
    Finds the minimum cuts for palindrome partitioning using recursion.

    Time Complexity: O(2^n) (Exponential)
    Space Complexity: O(n) (Recursion depth)
    """
    if i >= j or is_palindrome(s, i, j):
        return 0  # No partition needed

    min_cuts = float("inf")
    for k in range(i, j):
        if is_palindrome(s, i, k):  # Cut only if left part is palindrome
            cuts = 1 + min_partitions_recursive(s, k + 1, j)
            min_cuts = min(min_cuts, cuts)

    return min_cuts


# Example Usage
s = "abcbm"
print(
    "Minimum Partitions (Recursion):", min_partitions_recursive(s, 0, len(s) - 1)
)  # Output: 2


def min_partitions_dp(s):
    """
    Finds the minimum cuts for palindrome partitioning using dynamic programming.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(s)
    dp = [0] * n
    is_palindrome = [[False] * n for _ in range(n)]

    # Precompute palindrome substrings
    for j in range(n):
        min_cuts = j  # Max cuts needed = length - 1
        for i in range(j + 1):
            if s[i] == s[j] and (j - i <= 1 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
                min_cuts = 0 if i == 0 else min(min_cuts, dp[i - 1] + 1)
        dp[j] = min_cuts

    return dp[n - 1]


# Example Usage
s = "abcbm"
print("Minimum Partitions (DP):", min_partitions_dp(s))  # Output: 2
