import heapq


def prims_mst(graph):
    """
    Implements Prim's Algorithm to find the Minimum Spanning Tree (MST).

    Time Complexity: O(E log V)  (Using Min Heap)
    Space Complexity: O(V + E)  (Adjacency List + Min Heap)
    """
    start_node = 0  # Start from node 0 (arbitrary)
    mst = []
    visited = set()
    min_heap = [(0, start_node, -1)]  # (weight, current node, parent node)

    while len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue  # Skip if node is already in MST

        visited.add(node)
        if parent != -1:
            mst.append((parent, node, weight))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst  # List of MST edges (u, v, weight)


# Example Usage
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)],
}
print(prims_mst(graph))


class DisjointSet:
    """Implements Union-Find with Path Compression & Union by Rank."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path Compression
        return self.parent[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal_mst(edges, num_nodes):
    """
    Implements Kruskal's Algorithm to find the Minimum Spanning Tree (MST).

    Time Complexity: O(E log E) + O(E α(V))  (Sorting + Disjoint Set)
    Space Complexity: O(V + E)
    """
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(num_nodes)
    mst = []

    for u, v, weight in edges:
        if ds.union(u, v):  # Add edge if it doesn’t form a cycle
            mst.append((u, v, weight))
        if len(mst) == num_nodes - 1:
            break

    return mst  # List of MST edges (u, v, weight)


# Example Usage
edges = [(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
num_nodes = 5
print(kruskal_mst(edges, num_nodes))
