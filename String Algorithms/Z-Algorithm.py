def z_algorithm(s):
    """
    Computes the Z-array for string s.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        s (str): Input string.

    Returns:
        list: The Z-array where Z[i] is the length of the longest substring
              starting from s[i] that matches the prefix of s.
    """
    n = len(s)
    Z = [0] * n
    l, r, k = 0, 0, 0

    # Loop through the string from index 1 to n-1
    for i in range(1, n):
        if i > r:
            # Start a new Z-box
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            # We are within a Z-box
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1

    return Z


def pattern_search(text, pattern):
    """
    Finds all occurrences of a pattern in a text using the Z-Algorithm.

    Time Complexity: O(n + m), where n = len(text) and m = len(pattern)
    Space Complexity: O(n + m)

    Args:
        text (str): The main text to search within.
        pattern (str): The pattern to search for.

    Returns:
        list: List of starting indices where the pattern occurs in the text.
    """
    combined_string = pattern + "$" + text
    z_array = z_algorithm(combined_string)

    pattern_length = len(pattern)
    result = []

    for i in range(len(pattern) + 1, len(z_array)):
        if z_array[i] == pattern_length:
            result.append(i - pattern_length - 1)

    return result


# 🚀 Example Usage
text = "ababcababcababc"
pattern = "ababc"
result = pattern_search(text, pattern)

print(f"Pattern found at indices: {result}")
