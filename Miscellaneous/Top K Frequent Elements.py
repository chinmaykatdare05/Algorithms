from collections import Counter
import heapq


def top_k_frequent(nums, k):
    """
    Finds the top K frequent elements in the list.

    Args:
    nums (List[int]): List of integers.
    k (int): Number of top frequent elements to return.

    Returns:
    List[int]: List of the top K frequent elements.

    Time Complexity:
    - Counting frequency: O(n)
    - Building heap: O(n log k)
    - Extracting top k elements: O(k log k)
    Overall: O(n log k)

    Space Complexity: O(n) for the frequency map and heap.
    """

    # Count frequencies of each number
    count = Counter(nums)

    # Use a heap to get the top k elements
    return heapq.nlargest(k, count.keys(), key=count.get)


# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))  # Output: [1, 2]
