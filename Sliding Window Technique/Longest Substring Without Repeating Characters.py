def longest_unique_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: Length of the longest substring without repeating characters.

    Time Complexity: O(n)
    Space Complexity: O(min(n, m)), where n is the string length and m is the character set size (e.g., 26 for lowercase letters).
    """

    # Track the last seen position of characters
    char_index = {}
    left = 0
    max_length = 0

    # Expand the window by moving 'right'
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to avoid repeating characters
            left = char_index[s[right]] + 1

        # Update the latest position of the current character
        char_index[s[right]] = right

        # Calculate the length of the current valid window
        max_length = max(max_length, right - left + 1)

    return max_length


# 🔥 Test Cases
print(longest_unique_substring("abcabcbb"))  # Expected Output: 3 ("abc")
print(longest_unique_substring("bbbbb"))  # Expected Output: 1 ("b")
print(longest_unique_substring("pwwkew"))  # Expected Output: 3 ("wke")
print(longest_unique_substring(""))  # Expected Output: 0
