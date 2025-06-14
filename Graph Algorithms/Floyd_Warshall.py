def floyd_warshall(graph):
    """
    Implements Floyd-Warshall algorithm to find the shortest paths between all pairs of nodes.

    Time Complexity: O(V^3)
        - Three nested loops iterate over all pairs of vertices and intermediate nodes.

    Space Complexity: O(V^2)
        - Space for the distance matrix.

    Args:
        graph (list of lists): Adjacency matrix representation of the graph.
                               graph[i][j] is the weight from node i to node j.
                               Use float('inf') for no direct path between nodes.

    Returns:
        list: Distance matrix with shortest paths between all pairs of nodes.
              If dist[i][j] == float('inf'), no path exists between i and j.
    """
    V = len(graph)
    # Initialize distance matrix with input graph
    dist = [row[:] for row in graph]

    # Consider each node as an intermediate point one by one
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # If path through vertex k is shorter than the direct path from i to j
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example graph represented as an adjacency matrix
# Use float('inf') to represent no direct path
graph = [
    [0, 3, float("inf"), 5],
    [2, 0, float("inf"), 4],
    [float("inf"), 1, 0, float("inf")],
    [float("inf"), float("inf"), 2, 0],
]

shortest_paths = floyd_warshall(graph)

# Display the result
print("All Pairs Shortest Path Matrix:")
for row in shortest_paths:
    print(row)
