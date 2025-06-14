class DisjointSet:
    """
    Disjoint Set with Union by Rank and Path Compression.
    """

    def __init__(self, n):
        """Initialize parent and rank for 'n' elements."""
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        """Find the root of node 'x' with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union two sets by rank."""
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


def kruskal(graph):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST).

    Parameters:
    - graph: List of edges (u, v, weight)

    Time Complexity: O(E * logE), where E is the number of edges (due to sorting).
    Space Complexity: O(V + E), where V is the number of vertices.

    Returns:
    - Total weight of MST
    - List of edges in the MST
    """

    # Step 1: Sort edges by weight
    graph.sort(key=lambda x: x[2])

    # Initialize Union-Find structure
    nodes = set()
    for u, v, _ in graph:
        nodes.update([u, v])

    ds = DisjointSet(len(nodes))
    mst_weight = 0
    mst_edges = []

    # Step 2: Process edges one by one
    for u, v, weight in graph:
        # If u and v are in different components, include this edge in MST
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges


# Example usage:
graph = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 6),
    (2, 3, 8),
    (2, 4, 3),
    (3, 4, 9),
]

mst_weight, mst_edges = kruskal(graph)
print("Minimum Spanning Tree Weight:", mst_weight)
print("Edges in the MST:", mst_edges)
