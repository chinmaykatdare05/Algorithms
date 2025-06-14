import heapq


def dijkstra(graph, start):
    """
    Implements Dijkstra's Algorithm to find the shortest path from a start node to all other nodes in a weighted graph.

    Time Complexity: O((V + E) * log(V))
        - V: Number of vertices
        - E: Number of edges
        - Each node is processed once, and each push/pop operation on the priority queue takes log(V) time.

    Space Complexity: O(V)
        - Distance dictionary and priority queue store all nodes.

    Args:
        graph (dict): Weighted adjacency list where graph[u] = [(v, weight), ...].
        start (int): The starting node for the algorithm.

    Returns:
        dict: Shortest distances from the start node to each node.
    """

    # Priority queue for (distance, node)
    priority_queue = [(0, start)]

    # Track shortest distances from start node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded one, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example weighted graph (adjacency list)
graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

start_node = 0
print(f"Shortest paths from node {start_node}:")
print(dijkstra(graph, start_node))
