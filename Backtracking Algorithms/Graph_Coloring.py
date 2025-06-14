def is_safe(graph, node, color, colors):
    """
    Checks if the current color assignment is valid for a node.

    Time Complexity: O(N) - Checking all adjacent nodes.
    Space Complexity: O(1).

    Args:
        graph (List[List[int]]): Adjacency matrix representation of graph.
        node (int): Current node index.
        color (int): Color to assign.
        colors (List[int]): Assigned colors.

    Returns:
        bool: True if coloring is valid, False otherwise.
    """
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False  # Adjacent node has the same color
    return True


def graph_coloring_util(graph, m, colors, node):
    """
    Utilizes backtracking to solve the m-coloring problem.

    Time Complexity: O(m^N) - Worst case (trying all colors for all nodes).
    Space Complexity: O(N) - Storing color assignments.

    Args:
        graph (List[List[int]]): Adjacency matrix.
        m (int): Maximum number of colors.
        colors (List[int]): Color assignments.
        node (int): Current node index.

    Returns:
        bool: True if a valid coloring exists, False otherwise.
    """
    if node == len(graph):  # Base case: all nodes are colored
        return True

    # Try assigning each color (1 to m)
    for color in range(1, m + 1):
        if is_safe(graph, node, color, colors):
            colors[node] = color  # Assign color

            if graph_coloring_util(graph, m, colors, node + 1):
                return True  # Proceed to next node

            colors[node] = 0  # Backtrack if coloring fails

    return False  # No valid coloring found


def graph_coloring(graph, m):
    """
    Solves the Graph Coloring problem using Backtracking.

    Args:
        graph (List[List[int]]): Adjacency matrix representation.
        m (int): Number of colors.

    Returns:
        List[int] | str: List of color assignments or "No solution".
    """
    n = len(graph)
    colors = [0] * n  # Initialize color array

    if graph_coloring_util(graph, m, colors, 0):
        return colors  # Return valid color assignment

    return "No solution"  # No valid coloring found


# Example Usage
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3  # Maximum colors allowed

print(graph_coloring(graph, m))
