class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) for range sum queries and updates.

    Time Complexity:
        - Build: O(n)
        - Update: O(log n)
        - Prefix Sum Query: O(log n)
    Space Complexity: O(n)
    """

    def __init__(self, size):
        """
        Initializes a Fenwick Tree with a given size.
        """
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """
        Updates the tree with a value change (delta) at the given index.
        :param index: int - index (1-based) where the update happens
        :param delta: int - value to add (can be negative for reduction)
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Move to the next responsible node

    def prefix_sum(self, index):
        """
        Computes the prefix sum from index 1 to the given index.
        :param index: int - index (1-based) to compute the prefix sum up to
        :return: int - prefix sum result
        """
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Move to parent node
        return result

    def range_sum(self, left, right):
        """
        Computes the sum of elements within a given range [left, right].
        :param left: int - start of the range (1-based index)
        :param right: int - end of the range (1-based index)
        :return: int - sum of elements in range [left, right]
        """
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


# 🎯 **Example Usage**

arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

# Initialize Fenwick Tree
ft = FenwickTree(len(arr))

# Build the tree
for i, val in enumerate(arr):
    ft.update(i + 1, val)

# Query prefix sum up to index 5
print("Prefix sum of first 5 elements:", ft.prefix_sum(5))  # Output: 15

# Query range sum from index 3 to 7
print("Range sum from index 3 to 7:", ft.range_sum(3, 7))  # Output: 11

# Update index 4 by adding 3
ft.update(4, 3)

# New prefix sum after update
print("New prefix sum of first 5 elements:", ft.prefix_sum(5))  # Output: 18
