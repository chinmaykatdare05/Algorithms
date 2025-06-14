def is_safe(v, graph, path, pos):
    """
    Checks if vertex v can be added to the Hamiltonian path.

    Time Complexity: O(N) - Checking adjacency and uniqueness.
    Space Complexity: O(1).

    Args:
        v (int): Current vertex.
        graph (List[List[int]]): Adjacency matrix representation.
        path (List[int]): Hamiltonian path.
        pos (int): Current position in the path.

    Returns:
        bool: True if v can be added, False otherwise.
    """
    if graph[path[pos - 1]][v] == 0:  # No edge exists
        return False
    if v in path:  # Vertex already visited
        return False
    return True


def hamiltonian_path_util(graph, path, pos):
    """
    Utilizes backtracking to find a Hamiltonian Path.

    Time Complexity: O(N!) - Worst case (all permutations checked).
    Space Complexity: O(N) - Path storage.

    Args:
        graph (List[List[int]]): Adjacency matrix.
        path (List[int]): Current Hamiltonian path.
        pos (int): Position in path.

    Returns:
        bool: True if a valid Hamiltonian Path exists, False otherwise.
    """
    if pos == len(graph):  # Base case: All vertices are in the path
        return True

    # Try all vertices as the next step
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v  # Add vertex to path

            if hamiltonian_path_util(graph, path, pos + 1):
                return True  # Continue exploring

            path[pos] = -1  # Backtrack

    return False  # No valid path found


def find_hamiltonian_path(graph):
    """
    Finds a Hamiltonian Path in the graph.

    Args:
        graph (List[List[int]]): Adjacency matrix representation.

    Returns:
        List[int] | str: Hamiltonian path or "No solution".
    """
    n = len(graph)
    path = [-1] * n  # Initialize path with -1
    path[0] = 0  # Start from vertex 0

    if hamiltonian_path_util(graph, path, 1):
        return path  # Return the found Hamiltonian Path

    return "No solution"


def find_hamiltonian_circuit(graph):
    """
    Finds a Hamiltonian Circuit in the graph.

    Args:
        graph (List[List[int]]): Adjacency matrix.

    Returns:
        List[int] | str: Hamiltonian Circuit or "No solution".
    """
    path = find_hamiltonian_path(graph)

    if path == "No solution":
        return "No solution"

    # Check if there is an edge back to the start vertex
    if graph[path[-1]][path[0]] == 1:
        return path + [path[0]]  # Form a cycle

    return "No solution"


# Example Usage
graph = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0],
]

print("Hamiltonian Path:", find_hamiltonian_path(graph))
print("Hamiltonian Circuit:", find_hamiltonian_circuit(graph))
