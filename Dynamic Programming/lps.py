def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence using DP.

    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base Case: Single letters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the DP table bottom-up
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]  # The longest palindrome in the full string


# Example Usage
print(longest_palindromic_subsequence("bbbab"))  # Output: 4
print(longest_palindromic_subsequence("cbbd"))  # Output: 2


def longest_palindromic_subsequence_optimized(s):
    """
    Optimized DP approach with O(N) space.

    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    n = len(s)
    prev = [0] * n  # Previous row
    curr = [0] * n  # Current row

    # Base case: Single characters are palindromes
    for i in range(n):
        prev[i] = 1

    # Bottom-up DP with space optimization
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                curr[i] = 2 + prev[i + 1]
            else:
                curr[i] = max(prev[i], curr[i + 1])

        prev = curr[:]

    return prev[0]


# Example Usage
print(longest_palindromic_subsequence_optimized("bbbab"))  # Output: 4
print(longest_palindromic_subsequence_optimized("cbbd"))  # Output: 2
