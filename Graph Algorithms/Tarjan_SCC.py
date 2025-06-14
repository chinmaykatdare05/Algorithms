def tarjans_scc(graph):
    """
    Implements Tarjan's Algorithm to find all Strongly Connected Components (SCCs)
    in a directed graph.

    Time Complexity: O(V + E)
        - Each node and edge is processed once.

    Space Complexity: O(V)
        - For discovery time, low-link values, stack, and visited tracking.

    Args:
        graph (dict): Adjacency list representation of the graph.

    Returns:
        list: A list of SCCs, where each SCC is represented as a list of nodes.
    """
    n = len(graph)
    ids = [-1] * n  # Track node discovery times
    low = [-1] * n  # Track the smallest reachable node ID
    visited = [False] * n
    stack = []
    sccs = []

    # Mutable counters to track the current discovery time
    current_id = [0]

    def dfs(node):
        """Depth-first search to find SCCs."""
        ids[node] = low[node] = current_id[0]
        current_id[0] += 1
        stack.append(node)
        visited[node] = True

        # Explore all neighbors
        for neighbor in graph[node]:
            if ids[neighbor] == -1:
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
            elif visited[neighbor]:
                low[node] = min(low[node], ids[neighbor])

        # If a node is the root of an SCC, pop the stack to form an SCC
        if ids[node] == low[node]:
            scc = []
            while True:
                current_node = stack.pop()
                visited[current_node] = False
                scc.append(current_node)
                if current_node == node:
                    break
            sccs.append(scc)

    # Run DFS on all unvisited nodes
    for node in range(n):
        if ids[node] == -1:
            dfs(node)

    return sccs


# Example graph represented as an adjacency list
graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [], 5: [6], 6: [5]}

sccs = tarjans_scc(graph)

# Display the result
print("Strongly Connected Components:", sccs)
