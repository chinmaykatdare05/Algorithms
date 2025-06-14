def edit_distance_recursive(word1, word2, i=None, j=None):
    """
    Finds the minimum edit distance using recursion.

    Time Complexity: O(3^n) (Exponential)
    Space Complexity: O(m + n) (Recursion depth)
    """
    if i is None:
        i = len(word1)
    if j is None:
        j = len(word2)

    # Base cases
    if i == 0:
        return j  # Need to insert all characters of word2
    if j == 0:
        return i  # Need to delete all characters of word1

    # If last characters match, move to the previous characters
    if word1[i - 1] == word2[j - 1]:
        return edit_distance_recursive(word1, word2, i - 1, j - 1)

    # Otherwise, try all three operations and take the minimum
    return 1 + min(
        edit_distance_recursive(word1, word2, i - 1, j),  # Deletion
        edit_distance_recursive(word1, word2, i, j - 1),  # Insertion
        edit_distance_recursive(word1, word2, i - 1, j - 1),  # Substitution
    )


# Example Usage
word1 = "horse"
word2 = "ros"
print("Edit Distance (Recursion):", edit_distance_recursive(word1, word2))  # Output: 3


def edit_distance_dp(word1, word2):
    """
    Finds the minimum edit distance using Dynamic Programming.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters of word1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters of word2

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


# Example Usage
print("Edit Distance (DP):", edit_distance_dp("horse", "ros"))  # Output: 3


def edit_distance_space_optimized(word1, word2):
    """
    Finds the minimum edit distance using space-optimized DP.

    Time Complexity: O(m * n)
    Space Complexity: O(n) (Only storing previous row)
    """
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr  # Move to next row

    return prev[n]


# Example Usage
print(
    "Edit Distance (Space Optimized DP):", edit_distance_space_optimized("horse", "ros")
)  # Output: 3
