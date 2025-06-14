class DisjointSet:
    """
    Disjoint Set (Union-Find) with Union by Rank/Size and Path Compression.

    Time Complexity:
    - Union by Rank/Size: O(α(n)) — Inverse Ackermann function (very close to O(1))
    - Find with Path Compression: O(α(n))
    - Space Complexity: O(n) — For parent and rank/size arrays
    """

    def __init__(self, n):
        """Initialize the parent and rank/size arrays for 'n' elements."""
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        """Find the representative (root) of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, x, y):
        """Perform union of two sets by rank."""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Attach the smaller tree under the larger one
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def union_by_size(self, x, y):
        """Perform union of two sets by size (alternative approach)."""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Attach smaller set under larger set
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]

    def connected(self, x, y):
        """Check if two elements belong to the same set."""
        return self.find(x) == self.find(y)


# Example usage:
ds = DisjointSet(7)

# Union operations
ds.union_by_rank(1, 2)
ds.union_by_rank(2, 3)
ds.union_by_rank(4, 5)
ds.union_by_rank(6, 7)
ds.union_by_rank(5, 6)

# Check connected components
print(ds.connected(1, 3))  # Output: True
print(ds.connected(4, 7))  # Output: True
print(ds.connected(1, 7))  # Output: False
