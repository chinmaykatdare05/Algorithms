import heapq


class MedianFinder:
    def __init__(self):
        """Initialize two heaps: max-heap (left) and min-heap (right)."""
        self.left = []  # Max-heap (invert values to simulate max behavior)
        self.right = []  # Min-heap

    def add_num(self, num):
        """
        Add a number into the data stream.
        Time Complexity: O(log n)
        """
        # Push to max heap (invert num to simulate max-heap)
        heapq.heappush(self.left, -num)

        # Ensure the left heap's max is less than the right heap's min
        if self.left and self.right and (-self.left[0] > self.right[0]):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # Balance the heaps — ensure left has at most 1 extra element
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def find_median(self):
        """
        Find the median of the current data stream.
        Time Complexity: O(1)
        """
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2


# 🔥 Test the solution
stream = [5, 15, 1, 3]
median_finder = MedianFinder()

for num in stream:
    median_finder.add_num(num)
    print(f"Added {num}, Current Median: {median_finder.find_median()}")
