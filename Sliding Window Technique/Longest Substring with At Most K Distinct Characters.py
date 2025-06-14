def longest_substring_k_distinct(s, k):
    """
    Finds the length of the longest substring with at most K distinct characters.

    Args:
        s (str): The input string.
        k (int): Maximum number of distinct characters allowed.

    Returns:
        int: Length of the longest substring satisfying the condition.

    Time Complexity: O(n)
    Space Complexity: O(k) — to store at most K characters in the hashmap.
    """
    from collections import defaultdict

    # Edge case: if K is 0 or string is empty
    if k == 0 or not s:
        return 0

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    # Expand the window by moving 'right'
    for right in range(len(s)):
        char_count[s[right]] += 1

        # Shrink the window when we exceed K distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length


# 🔥 Test Cases
print(longest_substring_k_distinct("araaci", 2))  # Expected Output: 4 ("araa")
print(longest_substring_k_distinct("araaci", 1))  # Expected Output: 2 ("aa")
print(
    longest_substring_k_distinct("cbbebi", 3)
)  # Expected Output: 5 ("cbbeb" or "bbebi")
