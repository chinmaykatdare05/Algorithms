def topological_sort(graph):
    """
    Performs Topological Sort on a Directed Acyclic Graph (DAG).

    Time Complexity: O(V + E)
        - V: Number of vertices
        - E: Number of edges

    Space Complexity: O(V)
        - Stack stores all nodes once

    Args:
        graph (dict): Adjacency list representation of a directed graph.

    Returns:
        list: Nodes in topologically sorted order (if DAG).
              If a cycle is detected, returns an empty list.
    """
    visited = set()
    stack = []
    on_path = set()  # To detect cycles

    def dfs(node):
        """Helper function to perform DFS and track the topological order."""
        if node in on_path:
            raise ValueError("Cycle detected — Topological sort not possible!")

        if node not in visited:
            visited.add(node)
            on_path.add(node)  # Mark this node as being processed

            for neighbor in graph.get(node, []):
                dfs(neighbor)

            on_path.remove(node)  # Finished processing this node
            stack.append(node)

    # Call DFS for every unvisited node
    try:
        for node in graph:
            if node not in visited:
                dfs(node)

        # Return the nodes in reverse order of finishing times
        return stack[::-1]

    except ValueError as e:
        print(e)
        return []


# Example graph (DAG)
graph = {5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 1: [], 0: []}

print("Topological Sort Order:")
result = topological_sort(graph)
if result:
    print(result)
