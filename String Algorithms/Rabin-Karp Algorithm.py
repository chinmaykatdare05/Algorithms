def rabin_karp(text, pattern, prime=101):
    """
    Implements the Rabin-Karp algorithm to find all occurrences of a pattern in a text.

    Time Complexity:
        - Average case: O(N + M)
        - Worst case (hash collisions): O(N * M)
    Space Complexity: O(1) — Only a few integers are stored (pattern hash, rolling hash)

    Args:
        text (str): The main text to search within.
        pattern (str): The pattern to search for.
        prime (int): A prime number for better hash distribution (default: 101).

    Returns:
        list: A list of starting indices where the pattern occurs in the text.
    """
    d = 256  # Number of characters in the input alphabet (ASCII)
    n, m = len(text), len(pattern)
    pattern_hash = 0  # Hash value for pattern
    text_hash = 0  # Hash value for current text window
    h = 1
    matches = []

    # Calculate the hash multiplier for the leftmost character
    for _ in range(m - 1):
        h = (h * d) % prime

    # Calculate the initial hash values for the pattern and the first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Slide over the text
    for i in range(n - m + 1):
        # Check hash values first
        if pattern_hash == text_hash:
            # Verify by checking characters one by one (collision check)
            if text[i : i + m] == pattern:
                matches.append(i)

        # Calculate the hash for the next window by rolling
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # Ensure the hash is non-negative
            if text_hash < 0:
                text_hash += prime

    return matches


# 🚀 Example Usage
text = "ABCCDDAEFGABCDABCD"
pattern = "ABCD"
result = rabin_karp(text, pattern)

print(f"Pattern found at indices: {result}")
