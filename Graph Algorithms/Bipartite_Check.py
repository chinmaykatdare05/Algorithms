from collections import deque


def is_bipartite_bfs(graph):
    """
    Checks if a graph is bipartite using Breadth-First Search (BFS).

    Time Complexity: O(V + E)
        - Each node and edge is processed once.

    Space Complexity: O(V)
        - For the color array and BFS queue.

    Args:
        graph (dict): Adjacency list representation of the graph.

    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """
    n = len(graph)
    color = [-1] * n  # -1 means uncolored

    for start_node in range(n):
        if color[start_node] == -1:  # If node is unvisited
            queue = deque([start_node])
            color[start_node] = 0  # Start with color 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # Alternate color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return (
                            False  # Same color on both nodes means it's not bipartite
                        )
    return True


# 🎯 Example graph (Bipartite graph)
graph_bipartite = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

# 🚨 Non-bipartite graph
graph_non_bipartite = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

print("Bipartite (BFS):", is_bipartite_bfs(graph_bipartite))  # Output: True
print("Non-Bipartite (BFS):", is_bipartite_bfs(graph_non_bipartite))  # Output: False


def is_bipartite_dfs(graph):
    """
    Checks if a graph is bipartite using Depth-First Search (DFS).

    Time Complexity: O(V + E)
        - Each node and edge is processed once.

    Space Complexity: O(V)
        - For the color array and recursion stack.

    Args:
        graph (dict): Adjacency list representation of the graph.

    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """
    n = len(graph)
    color = [-1] * n

    def dfs(node, current_color):
        """Helper DFS function to color nodes."""
        color[node] = current_color
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - current_color):
                    return False
            elif color[neighbor] == color[node]:
                return False
        return True

    # Check each component (handles disconnected graphs too!)
    for node in range(n):
        if color[node] == -1:
            if not dfs(node, 0):
                return False

    return True


print("Bipartite (DFS):", is_bipartite_dfs(graph_bipartite))  # Output: True
print("Non-Bipartite (DFS):", is_bipartite_dfs(graph_non_bipartite))  # Output: False
