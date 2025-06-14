def dfs_recursive(graph, node, visited=None):
    """
    Performs Depth-First Search (DFS) recursively.

    DFS explores a branch fully before backtracking to explore other branches.

    Time Complexity:
        - O(V + E) where V = number of vertices, E = number of edges.
    Space Complexity:
        - O(V) in the worst case due to recursion stack.

    Parameters:
        graph (dict): The adjacency list representation of the graph.
        node (int/str): The starting node for DFS.
        visited (set): A set to track visited nodes.

    Returns:
        None: Prints the nodes in DFS traversal order.
    """
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Process the current node
        visited.add(node)

        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)


# Example usage
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
print("Recursive DFS Traversal:")
dfs_recursive(graph, "A")  # Output: A B D E F C


def dfs_iterative(graph, start):
    """
    Performs Depth-First Search (DFS) iteratively using an explicit stack.

    Instead of using recursion, this approach maintains a stack to simulate the DFS call stack.

    Time Complexity:
        - O(V + E) where V = number of vertices, E = number of edges.
    Space Complexity:
        - O(V) in the worst case due to stack storage.

    Parameters:
        graph (dict): The adjacency list representation of the graph.
        start (int/str): The starting node for DFS.

    Returns:
        None: Prints the nodes in DFS traversal order.
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the current node
            visited.add(node)
            stack.extend(
                reversed(graph.get(node, []))
            )  # Reverse to maintain correct order


# Example usage
print("\nIterative DFS Traversal:")
dfs_iterative(graph, "A")  # Output: A C F B E D
