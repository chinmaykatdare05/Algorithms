from collections import defaultdict


class Graph:
    """
    Represents an undirected graph and checks for Eulerian Path or Circuit.
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Adds an edge between node u and v."""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def _dfs_count(self, v, visited):
        """Helper DFS to count reachable vertices from a starting node."""
        visited[v] = True
        count = 1
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                count += self._dfs_count(neighbor, visited)
        return count

    def _is_connected(self):
        """Checks if all non-zero degree nodes are connected."""
        visited = {node: False for node in self.graph}
        start_node = next(
            (node for node in self.graph if len(self.graph[node]) > 0), None
        )

        # If there are no edges, the graph is trivially connected
        if start_node is None:
            return True

        # Perform DFS from the first non-zero degree node
        count = self._dfs_count(start_node, visited)

        # Check if all non-zero degree nodes were visited
        for node in self.graph:
            if len(self.graph[node]) > 0 and not visited[node]:
                return False

        return True

    def check_eulerian(self):
        """
        Checks whether the graph contains an Eulerian Path or Circuit.

        Time Complexity: O(V + E)
            - DFS to check connectivity and degree counting.

        Space Complexity: O(V)
            - For visited nodes and degree counting.

        Returns:
            str: "Eulerian Circuit", "Eulerian Path", "Not Eulerian"
        """
        if not self._is_connected():
            return "Not Eulerian"

        # Count nodes with odd degree
        odd_degree_nodes = sum(
            1 for node in self.graph if len(self.graph[node]) % 2 != 0
        )

        # Determine Eulerian type
        if odd_degree_nodes == 0:
            return "Eulerian Circuit"
        elif odd_degree_nodes == 2:
            return "Eulerian Path"
        else:
            return "Not Eulerian"


# 🚀 Example Usage
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
print("Graph 1:", g1.check_eulerian())  # Output: Eulerian Circuit

g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 0)
g2.add_edge(0, 4)
g2.add_edge(4, 5)
g2.add_edge(5, 0)
print("Graph 2:", g2.check_eulerian())  # Output: Eulerian Path

g3 = Graph()
g3.add_edge(0, 1)
g3.add_edge(1, 2)
print("Graph 3:", g3.check_eulerian())  # Output: Not Eulerian
