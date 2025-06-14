class SegmentTree:
    """
    Segment Tree implementation for range sum queries and point updates.
    """

    def __init__(self, arr):
        """
        Initialize the Segment Tree.
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """
        Build the Segment Tree recursively.
        """
        if start == end:
            # Leaf node stores the array element
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            # Build left and right children
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            # Internal node stores the sum of its children
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        """
        Perform range sum query on the range [l, r].
        """
        if r < start or l > end:
            # Completely outside the range
            return 0

        if l <= start and end <= r:
            # Completely inside the range
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, l, r)
        right_sum = self.query(2 * node + 2, mid + 1, end, l, r)

        return left_sum + right_sum

    def update(self, node, start, end, idx, value):
        """
        Perform point update to change arr[idx] to 'value'.
        """
        if start == end:
            # Leaf node: directly update the value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # If index lies in the left child
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                # If index lies in the right child
                self.update(2 * node + 2, mid + 1, end, idx, value)

            # Update the parent node after updating the child
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def range_sum(self, l, r):
        """
        Public method to query sum in range [l, r].
        """
        return self.query(0, 0, self.n - 1, l, r)

    def point_update(self, idx, value):
        """
        Public method to update a specific index with a new value.
        """
        self.update(0, 0, self.n - 1, idx, value)


# 🎯 **Example Usage**
arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)

# 🌟 Range sum query from index 1 to 4
print("Sum of values from index 1 to 4:", segment_tree.range_sum(1, 4))  # Output: 24

# 🔧 Point update: Change value at index 2 to 10
segment_tree.point_update(2, 10)

# 🔍 Range sum query after update
print(
    "Sum of values from index 1 to 4 after update:", segment_tree.range_sum(1, 4)
)  # Output: 29
