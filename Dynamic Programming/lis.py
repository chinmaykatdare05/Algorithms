def lis_dp(arr):
    """
    Finds the length of the Longest Increasing Subsequence (LIS) using Dynamic Programming.

    Time Complexity: O(n²) (Nested loops)
    Space Complexity: O(n) (For DP array)

    Parameters:
        arr (list): List of integers.

    Returns:
        int: Length of the longest increasing subsequence.
    """
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n  # Initialize LIS length to 1 for each element

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # If increasing, update LIS length
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The longest LIS found


# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("LIS Length (DP):", lis_dp(arr))  # Output: 6


from bisect import bisect_left


def lis_binary_search(arr):
    """
    Finds the length of the Longest Increasing Subsequence (LIS) using Binary Search and Greedy approach.

    Time Complexity: O(n log n) (Binary Search inside a loop)
    Space Complexity: O(n) (For LIS array)

    Parameters:
        arr (list): List of integers.

    Returns:
        int: Length of the longest increasing subsequence.
    """
    if not arr:
        return 0

    sub = []  # Stores the LIS elements (not the actual sequence)

    for num in arr:
        pos = bisect_left(sub, num)  # Find position using binary search
        if pos == len(sub):  # If num is largest, append it
            sub.append(num)
        else:  # Otherwise, replace the element
            sub[pos] = num

    return len(sub)


# Example usage
print("LIS Length (Binary Search):", lis_binary_search(arr))  # Output: 6
