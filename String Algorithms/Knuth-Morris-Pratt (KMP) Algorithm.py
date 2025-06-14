def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for KMP pattern matching.

    Time Complexity: O(M) — M is the length of the pattern
    Space Complexity: O(M)

    Args:
        pattern (str): The pattern to preprocess.

    Returns:
        list: The LPS array indicating the longest prefix that is also a suffix.
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Implements the KMP algorithm to find occurrences of a pattern in a given text.

    Time Complexity: O(N + M) — N is the length of the text, M is the length of the pattern
    Space Complexity: O(M) — For the LPS array

    Args:
        text (str): The main text where we search for the pattern.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of starting indices where the pattern occurs in the text.
    """
    if not pattern:
        return []  # Edge case: empty pattern

    lps = compute_lps(pattern)
    i = j = 0  # i -> text index, j -> pattern index
    matches = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


# 🚀 Example Usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)

print(f"Pattern found at indices: {result}")
