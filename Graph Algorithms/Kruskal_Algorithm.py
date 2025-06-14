class DisjointSet:
    """Helper class for Union-Find with path compression and union by rank."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        """Find the representative (root) of the set containing the node."""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        """Union two subsets by rank."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Attach smaller rank tree under the larger one
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(graph, n):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

    Time Complexity: O(E * log(E))
        - E: Number of edges (due to sorting the edges)
        - Union-Find operations take nearly constant time with path compression.

    Space Complexity: O(V + E)
        - V: Nodes for the Union-Find structure
        - E: Stores all edges.

    Args:
        graph (list of tuples): Each edge is represented as (weight, u, v).
        n (int): Number of nodes.

    Returns:
        list: Edges included in the MST and the total weight.
    """
    # Sort edges based on weight (greedy strategy)
    graph.sort()

    disjoint_set = DisjointSet(n)
    mst = []  # Store edges in MST
    total_weight = 0

    # Iterate through sorted edges
    for weight, u, v in graph:
        # If u and v are in different sets, add the edge to the MST
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v))
            total_weight += weight

    return mst, total_weight


# Example weighted, undirected graph (list of edges)
graph = [(1, 0, 1), (4, 0, 2), (3, 1, 2), (2, 1, 3), (5, 2, 3)]
n = 4  # Number of nodes (0 to 3)

mst, total_weight = kruskal(graph, n)
print("Minimum Spanning Tree Edges:", mst)
print("Total Weight:", total_weight)
