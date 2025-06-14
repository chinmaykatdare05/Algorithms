def longest_bitonic_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Step 1: Compute LIS for each index
    LIS = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # Step 2: Compute LDS for each index (traverse backwards)
    LDS = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                LDS[i] = max(LDS[i], LDS[j] + 1)

    # Step 3: Find maximum bitonic sequence length
    max_bitonic_length = 0
    for i in range(n):
        max_bitonic_length = max(max_bitonic_length, LIS[i] + LDS[i] - 1)

    return max_bitonic_length


# Example usage:
arr = [1, 11, 2, 10, 4, 5, 2, 1]
print("Length of Longest Bitonic Subsequence:", longest_bitonic_subsequence(arr))
