def build_suffix_array(s):
    """
    Builds the suffix array of a string using the prefix-doubling method.

    Time Complexity: O(n log^2 n)
    Space Complexity: O(n)
    """
    n = len(s)
    suffixes = sorted((s[i:], i) for i in range(n))
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array


def build_lcp_array(s, suffix_array):
    """
    Builds the LCP (Longest Common Prefix) array from the suffix array using Kasai's algorithm.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(s)
    rank = [0] * n
    lcp = [0] * n

    # Compute the rank of each suffix
    for i in range(n):
        rank[suffix_array[i]] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1

    return lcp


# 🚀 **Example Usage**

s = "banana"
suffix_array = build_suffix_array(s)
lcp_array = build_lcp_array(s, suffix_array)

print(f"String: {s}")
print(f"Suffix Array: {suffix_array}")
print(f"LCP Array: {lcp_array}")
