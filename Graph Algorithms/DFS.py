def dfs(graph, start, visited=None):
    """
    Performs Depth-First Search (DFS) on a graph starting from a given node.

    Time Complexity: O(V + E)
        - V: Number of vertices
        - E: Number of edges

    Space Complexity: O(V)
        - Due to the recursion stack (in the worst case, for a linear graph)

    Args:
        graph (dict): Adjacency list representing the graph.
        start (str/int): The starting node for DFS traversal.
        visited (set): A set to track visited nodes (default is None).

    Returns:
        list: The nodes visited in DFS order.
    """

    # Initialize visited set on first call
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)
    print(start, end=" ")

    # Visit all neighbors that haven’t been visited yet
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# Example graph (adjacency list)
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1, 5], 5: [2, 4]}

print("DFS traversal from node 0:")
dfs(graph, 0)
