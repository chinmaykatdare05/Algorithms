from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search (BFS) on a graph starting from a given node.

    Time Complexity: O(V + E)
        - V: Number of vertices
        - E: Number of edges

    Space Complexity: O(V)
        - Due to the queue and visited set

    Args:
        graph (dict): Adjacency list representing the graph.
        start (str/int): The starting node for BFS traversal.

    Returns:
        list: The nodes visited in BFS order.
    """
    visited = set()  # Track visited nodes
    queue = deque([start])  # Initialize queue with the starting node

    bfs_order = []

    # Process nodes level by level
    while queue:
        node = queue.popleft()

        # If node hasn't been visited, process it
        if node not in visited:
            print(node, end=" ")
            bfs_order.append(node)
            visited.add(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order


# Example graph (adjacency list)
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1, 5], 5: [2, 4]}

print("BFS traversal from node 0:")
bfs(graph, 0)
