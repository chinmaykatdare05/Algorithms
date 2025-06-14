def wildcard_matching(s, p):
    """
    Determines if the wildcard pattern p matches the string s.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns with '*' at the start
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Match one character
            elif p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # Match multiple or zero chars

    return dp[m][n]


# Example Usage
print(wildcard_matching("baaabab", "ba*a?"))  # Output: True
print(wildcard_matching("abcd", "a*d"))  # Output: False


def regex_matching(s, p):
    """
    Determines if the regex pattern p matches the string s.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty pattern matches empty string
    dp[0][0] = True

    # Handle patterns with '*' at the start
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "." or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Match single character
            elif p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]  # Zero occurrence of character before '*'
                if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] |= dp[i - 1][j]  # One or more occurrences

    return dp[m][n]


# Example Usage
print(regex_matching("aab", "c*a*b"))  # Output: True
print(regex_matching("mississippi", "mis*is*p*."))  # Output: False
