import heapq


def kth_largest(nums, k):
    """
    Find the Kth largest element in an array using a Min-Heap.

    Time Complexity: O(n log k)
    - Each insertion/deletion into the heap takes O(log k).
    - We maintain a heap of size k, iterating through n elements.

    Space Complexity: O(k)
    - The heap contains k elements at most.
    """

    # Maintain a min-heap of size k
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        # Ensure heap size is only k
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Root of the heap is the Kth largest element
    return min_heap[0]


# 🔥 Test the function
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 3
print(f"The {k}rd largest element is:", kth_largest(nums, k))


def kth_largest_sort(nums, k):
    return sorted(nums, reverse=True)[k - 1]
