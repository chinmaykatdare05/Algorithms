class DisjointSet:
    """
    Disjoint Set with Path Compression.

    Time Complexity:
    - Find with Path Compression: O(α(n)), where α is the Inverse Ackermann function (extremely close to O(1))
    - Space Complexity: O(n) — for parent and rank arrays.
    """

    def __init__(self, n):
        """Initialize the parent and rank arrays for 'n' elements."""
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        """
        Find the root of the set containing 'x' with path compression.

        Path Compression flattens the tree, ensuring future find operations are faster.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union two sets based on their roots."""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        """Check if two elements are connected (belong to the same set)."""
        return self.find(x) == self.find(y)


# Example usage:
ds = DisjointSet(7)

# Union operations
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)

# Check connections
print(ds.connected(1, 3))  # Output: True
print(ds.connected(4, 5))  # Output: True
print(ds.connected(1, 5))  # Output: False

# Path compression effect demonstration
print(
    ds.parent
)  # You’ll notice a flatter structure (more elements directly linked to root)
