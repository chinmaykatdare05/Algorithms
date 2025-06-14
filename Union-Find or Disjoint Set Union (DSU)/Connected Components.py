def dfs(node, graph, visited):
    """Perform DFS traversal and mark connected nodes."""
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def count_connected_components(graph, n):
    """
    Counts the number of connected components in an undirected graph.

    Parameters:
    - graph: Adjacency list representation of the graph.
    - n: Number of nodes.

    Time Complexity: O(V + E)
    Space Complexity: O(V)

    Returns:
    - Number of connected components
    """

    visited = [False] * n
    count = 0

    # Visit each node
    for node in range(n):
        if not visited[node]:
            # Start a new DFS from an unvisited node
            dfs(node, graph, visited)
            count += 1

    return count


# Example graph (0-based index)
graph = {0: [1, 2], 1: [0], 2: [0], 3: [4], 4: [3], 5: []}

n = 6
components = count_connected_components(graph, n)
print("Number of connected components:", components)


class DisjointSet:
    """Union-Find with Path Compression and Union by Rank."""

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank."""
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


def count_components_union_find(n, edges):
    """
    Count connected components using Union-Find.

    Time Complexity: O(E * α(V))
    Space Complexity: O(V)

    Returns:
    - Number of connected components
    """
    ds = DisjointSet(n)

    for u, v in edges:
        ds.union(u, v)

    # Count unique roots (representatives of each component)
    root_set = set(ds.find(i) for i in range(n))
    return len(root_set)


# Example graph represented as an edge list
n = 6
edges = [
    (0, 1),
    (0, 2),
    (3, 4),
]

components = count_components_union_find(n, edges)
print("Number of connected components (Union-Find):", components)
