def preprocess(s):
    """
    Preprocesses the string by inserting special characters to handle even-length palindromes uniformly.

    Args:
        s (str): The original string.

    Returns:
        str: Transformed string with separators.
    """
    return "#" + "#".join(s) + "#"


def manacher(s):
    """
    Manacher's Algorithm to find the longest palindromic substring in O(n) time.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring.
    """
    # Preprocess the string
    t = preprocess(s)
    n = len(t)
    p = [0] * n  # Array to store palindrome radii
    center = right = 0  # Current center and right boundary
    max_len = start_idx = 0

    # Process each character in the transformed string
    for i in range(n):
        # Mirror i around the current center
        mirror = 2 * center - i

        # If within a known palindrome boundary, use mirror's radius
        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around i
        while (
            i + p[i] + 1 < n
            and i - p[i] - 1 >= 0
            and t[i + p[i] + 1] == t[i - p[i] - 1]
        ):
            p[i] += 1

        # Update center and right boundary if we expand beyond the current right
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Track the maximum palindrome found
        if p[i] > max_len:
            max_len = p[i]
            start_idx = (i - max_len) // 2  # Convert back to original string index

    # Extract the longest palindrome from the original string
    return s[start_idx : start_idx + max_len]


# 🚀 Example Usage
s = "babad"
print(f"Longest Palindromic Substring: {manacher(s)}")  # Output: "bab" or "aba"

s2 = "cbbd"
print(f"Longest Palindromic Substring: {manacher(s2)}")  # Output: "bb"
