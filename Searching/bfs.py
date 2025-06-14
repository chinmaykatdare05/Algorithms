from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search (BFS) iteratively using a queue.

    BFS explores all neighbors of a node before moving to the next level.

    Time Complexity:
        - O(V + E) where V = number of vertices, E = number of edges.
    Space Complexity:
        - O(V) in the worst case (when all nodes are stored in the queue).

    Parameters:
        graph (dict): The adjacency list representation of the graph.
        start (int/str): The starting node for BFS.

    Returns:
        None: Prints the nodes in BFS traversal order.
    """
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()  # Dequeue the front element
        if node not in visited:
            print(node, end=" ")  # Process the current node
            visited.add(node)
            queue.extend(graph.get(node, []))  # Enqueue all unvisited neighbors


# Example usage
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
print("BFS Traversal:")
bfs(graph, "A")  # Output: A B C D E F
