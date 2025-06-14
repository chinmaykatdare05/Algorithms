import heapq


def dijkstra(graph, source):
    """
    Implements Dijkstra's Algorithm for Single Source Shortest Path.

    Time Complexity: O((V + E) log V)  (Using Min Heap)
    Space Complexity: O(V + E)  (Adjacency List + Distance Table)
    """
    # Initialize distances (∞ for all, 0 for source)
    distances = {node: float("inf") for node in graph}
    distances[source] = 0

    # Min-Heap: (distance, node)
    min_heap = [(0, source)]

    while min_heap:
        curr_distance, node = heapq.heappop(min_heap)

        # If a better path is already found, skip
        if curr_distance > distances[node]:
            continue

        # Relaxation step: Update neighbors
        for neighbor, weight in graph[node]:
            new_distance = curr_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


# Example Usage
graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: [(4, 3)], 4: []}
source = 0
print(dijkstra(graph, source))
