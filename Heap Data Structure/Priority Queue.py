import heapq


class PriorityQueue:
    """
    Priority Queue implementation using Python's heapq module (min-heap).
    Supports elements with priorities — lower values are higher priority.

    Time Complexity:
    - Insert: O(log n)
    - Get highest priority element: O(1)
    - Remove highest priority element: O(log n)

    Space Complexity: O(n), where n is the number of elements in the queue.
    """

    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        """
        Adds an item to the queue with a given priority.
        Lower priority number means higher priority.
        """
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        """Removes and returns the highest priority element."""
        if self.is_empty():
            return None
        return heapq.heappop(self.queue)[1]

    def peek(self):
        """Returns the highest priority element without removing it."""
        if self.is_empty():
            return None
        return self.queue[0][1]

    def is_empty(self):
        """Returns True if the queue is empty."""
        return len(self.queue) == 0

    def __str__(self):
        """Prints the queue (for debugging)."""
        return str([(item, priority) for priority, item in self.queue])


# 🔥 Test Priority Queue
pq = PriorityQueue()

pq.push("Task A", 2)
pq.push("Task B", 1)
pq.push("Task C", 3)

print("Priority Queue:", pq)  # Output: [('Task B', 1), ('Task A', 2), ('Task C', 3)]

print("Highest Priority Element:", pq.peek())  # Output: Task B (priority 1)
print("Pop:", pq.pop())  # Output: Task B (priority 1)
print("Priority Queue After Pop:", pq)  # Output: [('Task A', 2), ('Task C', 3)]

print("Is Empty?", pq.is_empty())  # Output: False
pq.pop()
pq.pop()
print("Is Empty After All Pops?", pq.is_empty())  # Output: True
