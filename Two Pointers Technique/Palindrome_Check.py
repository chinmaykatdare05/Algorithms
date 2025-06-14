def is_palindrome(s):
    """
    Checks if a given string or number (converted to string) is a palindrome.

    Time Complexity: O(n)
    - n: Length of the string.
    - Each character is compared once.

    Space Complexity: O(1)
    - Only pointers are stored, no extra data structures.

    Args:
    s (str/int): The input string or number to check.

    Returns:
    bool: True if it's a palindrome, False otherwise.
    """

    # Convert numbers to strings
    s = str(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Test cases
print("racecar:", is_palindrome("racecar"))  # True
print("hello:", is_palindrome("hello"))  # False
print("12321:", is_palindrome(12321))  # True
print("12345:", is_palindrome(12345))  # False
