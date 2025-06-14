class UnionFind:
    """
    A class to implement Disjoint Set Union (Union-Find) with Path Compression and Union by Rank.

    Time Complexity:
        - Find: O(α(n)), where α is the Inverse Ackermann function (very close to constant).
        - Union: O(α(n))

    Space Complexity: O(n), where n is the number of elements (each node has a parent and rank).
    """

    def __init__(self, size):
        # Initialize each node as its own parent (self-loop)
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node):
        """
        Find the root representative of a node, with path compression.
        """
        if self.parent[node] != node:
            # Path compression: make node point directly to its root
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        """
        Union two sets by rank — attach smaller tree under the larger tree.
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Attach smaller rank tree under larger rank tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                # Same rank: arbitrarily choose one and increase its rank
                self.parent[root2] = root1
                self.rank[root1] += 1


# Example Usage
uf = UnionFind(7)

# Union operations
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 5)

# Find operations (checking connected components)
print("Are 1 and 3 connected?", uf.find(1) == uf.find(3))  # True
print("Are 1 and 4 connected?", uf.find(1) == uf.find(4))  # False

# Connecting two different components
uf.union(3, 4)
print("Are 1 and 5 connected now?", uf.find(1) == uf.find(5))  # True
