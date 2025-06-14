from collections import Counter


def min_window_substring(s, t):
    """
    Finds the minimum window substring in 's' that contains all characters of 't'.

    Args:
        s (str): The input string to search within.
        t (str): The target string containing the required characters.

    Returns:
        str: The smallest substring that contains all characters of 't', or "" if no such substring exists.

    Time Complexity: O(n)
    Space Complexity: O(m), where n is the length of 's' and m is the length of 't' (for the frequency count).
    """

    if not t or not s:
        return ""

    # Count frequency of characters in target string
    target_count = Counter(t)
    required = len(target_count)

    # Sliding window pointers and state tracking
    left, right = 0, 0
    formed = 0
    window_count = {}
    min_length = float("inf")
    min_window = (0, 0)

    # Expand the window by moving 'right'
    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        # Check if current character satisfies target frequency
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Try shrinking the window from the left
        while left <= right and formed == required:
            char = s[left]

            # Update the minimum window if a smaller one is found
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = (left, right)

            # Shrink window by reducing the left character count
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1

            left += 1

        # Expand window further
        right += 1

    # Return the minimum window substring
    return s[min_window[0] : min_window[1] + 1] if min_length != float("inf") else ""


# 🔥 Test Cases
print(min_window_substring("ADOBECODEBANC", "ABC"))  # Expected Output: "BANC"
print(min_window_substring("a", "a"))  # Expected Output: "a"
print(min_window_substring("a", "aa"))  # Expected Output: ""
print(min_window_substring("abc", "cba"))  # Expected Output: "abc"
