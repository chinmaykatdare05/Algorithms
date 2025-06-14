import heapq


class MinHeap:
    """
    MinHeap implementation using Python's heapq library (which is a min-heap by default).

    Time Complexity:
    - Insert: O(log n)
    - Get Min: O(1)
    - Extract Min: O(log n)

    Space Complexity: O(n), where n is the number of elements in the heap.
    """

    def __init__(self):
        self.heap = []

    def push(self, val):
        """Inserts an element into the min heap."""
        heapq.heappush(self.heap, val)

    def pop(self):
        """Removes and returns the smallest element (root) from the heap."""
        return heapq.heappop(self.heap)

    def peek(self):
        """Returns the smallest element without removing it."""
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


class MaxHeap:
    """
    MaxHeap implementation by inverting values in a MinHeap (Python's heapq).

    Time Complexity:
    - Insert: O(log n)
    - Get Max: O(1)
    - Extract Max: O(log n)

    Space Complexity: O(n), where n is the number of elements in the heap.
    """

    def __init__(self):
        self.heap = []

    def push(self, val):
        """Inserts an element into the max heap (stored as negative values)."""
        heapq.heappush(self.heap, -val)

    def pop(self):
        """Removes and returns the largest element from the heap."""
        return -heapq.heappop(self.heap)

    def peek(self):
        """Returns the largest element without removing it."""
        return -self.heap[0]

    def __str__(self):
        return str([-h for h in self.heap])


# 🧠 Test MinHeap
min_heap = MinHeap()
min_heap.push(10)
min_heap.push(4)
min_heap.push(15)
min_heap.push(7)

print("MinHeap:", min_heap)  # Output: [4, 7, 15, 10]
print("MinHeap Root:", min_heap.peek())  # Output: 4
print("Extract Min:", min_heap.pop())  # Output: 4
print("MinHeap After Extract:", min_heap)  # Output: [7, 10, 15]

# 🔥 Test MaxHeap
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(4)
max_heap.push(15)
max_heap.push(7)

print("\nMaxHeap:", max_heap)  # Output: [15, 7, 10, 4]
print("MaxHeap Root:", max_heap.peek())  # Output: 15
print("Extract Max:", max_heap.pop())  # Output: 15
print("MaxHeap After Extract:", max_heap)  # Output: [10, 7, 4]
