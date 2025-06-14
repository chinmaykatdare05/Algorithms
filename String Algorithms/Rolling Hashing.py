def rolling_hash(text, pattern):
    """
    Rolling Hash-based pattern search (like Rabin-Karp).

    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Args:
        text (str): The main text to search within.
        pattern (str): The pattern to search for.

    Returns:
        list: List of starting indices where the pattern occurs in the text.
    """
    n, m = len(text), len(pattern)
    base = 31
    mod = 10**9 + 7

    # Compute the hash of the pattern and the first window in text
    pattern_hash = (
        sum((ord(pattern[i]) * pow(base, m - i - 1, mod)) for i in range(m)) % mod
    )
    current_hash = (
        sum((ord(text[i]) * pow(base, m - i - 1, mod)) for i in range(m)) % mod
    )

    # Precompute base^(m-1) % mod for rolling
    base_m = pow(base, m - 1, mod)

    result = []

    # Sliding window over the text
    for i in range(n - m + 1):
        # Check if hashes match (and verify the strings to avoid collisions)
        if current_hash == pattern_hash and text[i : i + m] == pattern:
            result.append(i)

        # Roll the hash to the next window (if not at the end)
        if i < n - m:
            current_hash = (
                (current_hash - ord(text[i]) * base_m) * base + ord(text[i + m])
            ) % mod

            # Ensure the hash is non-negative
            if current_hash < 0:
                current_hash += mod

    return result


# 🚀 Example Usage
text = "ababcababcababc"
pattern = "ababc"
result = rolling_hash(text, pattern)

print(f"Pattern found at indices: {result}")
