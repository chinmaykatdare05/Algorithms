def bellman_ford(graph, start):
    """
    Implements the Bellman-Ford algorithm to find the shortest path from a start node to all other nodes.
    It handles graphs with **negative weights** but **detects negative weight cycles**.

    Time Complexity: O(V * E)
        - V: Number of vertices
        - E: Number of edges

    Space Complexity: O(V)
        - Stores distances to all nodes.

    Args:
        graph (list of tuples): Each edge is represented as (u, v, weight).
        start (int): The starting node.

    Returns:
        tuple: (distances, negative_cycle)
        - distances: Dictionary of shortest distances from the start node.
        - negative_cycle: True if a negative weight cycle is detected, otherwise False.
    """

    # Step 1: Initialize distances
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Step 2: Relax edges repeatedly (V-1 times)
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if (
                    distances[u] != float("inf")
                    and distances[u] + weight < distances[v]
                ):
                    distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Negative weight cycle detected!")
                return distances, True

    return distances, False


# Example graph (adjacency list with weights)
graph = {0: [(1, 4), (2, 5)], 1: [(3, -2)], 2: [(1, -3), (3, 3)], 3: []}

start_node = 0
distances, has_cycle = bellman_ford(graph, start_node)

if not has_cycle:
    print(f"Shortest paths from node {start_node}: {distances}")
