def lcs_dp(str1, str2):
    """
    Finds the length of the Longest Common Subsequence (LCS) using Dynamic Programming.

    Time Complexity: O(m × n) (Nested loops over both strings)
    Space Complexity: O(m × n) (For DP table)

    Parameters:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        int: Length of the longest common subsequence.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # Initialize DP table

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:  # Matching characters
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # Mismatch case
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example usage
str1 = "AGGTAB"
str2 = "GXTXAYB"
print("LCS Length (DP):", lcs_dp(str1, str2))  # Output: 4


def lcs_recursive(str1, str2, m, n):
    """
    Finds the length of the Longest Common Subsequence (LCS) using Recursion.

    Time Complexity: O(2^n) (Exponential growth)
    Space Complexity: O(m + n) (Recursive stack)

    Parameters:
        str1 (str): First string.
        str2 (str): Second string.
        m (int): Length of str1.
        n (int): Length of str2.

    Returns:
        int: Length of the longest common subsequence.
    """
    if m == 0 or n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:  # Matching case
        return 1 + lcs_recursive(str1, str2, m - 1, n - 1)
    else:  # Mismatch case
        return max(
            lcs_recursive(str1, str2, m - 1, n), lcs_recursive(str1, str2, m, n - 1)
        )


# Example usage
print(
    "LCS Length (Recursive):", lcs_recursive(str1, str2, len(str1), len(str2))
)  # Output: 4


def lcs_space_optimized(str1, str2):
    """
    Finds the length of the Longest Common Subsequence (LCS) using Space-Optimized Dynamic Programming.

    Time Complexity: O(m × n) (Nested loops over both strings)
    Space Complexity: O(n) (Optimized to store only two rows)

    Parameters:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        int: Length of the longest common subsequence.
    """
    m, n = len(str1), len(str2)
    prev = [0] * (n + 1)  # Store previous row

    for i in range(1, m + 1):
        curr = [0] * (n + 1)  # Current row
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:  # Matching characters
                curr[j] = 1 + prev[j - 1]
            else:  # Mismatch case
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr  # Move to the next row

    return prev[n]


# Example usage
print("LCS Length (Space Optimized DP):", lcs_space_optimized(str1, str2))  # Output: 4


def print_lcs(str1, str2):
    """
    Prints the Longest Common Subsequence (LCS) using Dynamic Programming.

    Time Complexity: O(m × n)
    Space Complexity: O(m × n) (For DP table and sequence reconstruction)

    Parameters:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        str: The longest common subsequence.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Traceback to reconstruct LCS
    i, j = m, n
    lcs_str = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:  # Matching characters
            lcs_str.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

    return "".join(reversed(lcs_str))


# Example usage
print("LCS Sequence:", print_lcs(str1, str2))  # Output: "GTAB"
