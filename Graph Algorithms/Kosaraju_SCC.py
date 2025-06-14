def kosaraju_scc(graph):
    """
    Implements Kosaraju's Algorithm to find all Strongly Connected Components (SCCs)
    in a directed graph.

    Time Complexity: O(V + E)
        - Two DFS traversals of the graph.

    Space Complexity: O(V + E)
        - To store the graph, stack, and visited nodes.

    Args:
        graph (dict): Adjacency list representation of the graph.

    Returns:
        list: A list of SCCs, where each SCC is represented as a list of nodes.
    """

    # Step 1: First DFS to determine the finishing order of nodes
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    # Step 2: Transpose the graph (reverse all edges)
    def transpose(graph):
        transposed_graph = {node: [] for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                transposed_graph[neighbor].append(node)
        return transposed_graph

    # Step 3: Second DFS on the transposed graph to find SCCs
    def dfs_transposed(node, visited, scc, transposed_graph):
        visited.add(node)
        scc.append(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs_transposed(neighbor, visited, scc, transposed_graph)

    # Step 1: First DFS to get finishing times
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    # Step 2: Transpose the graph
    transposed_graph = transpose(graph)

    # Step 3: Process nodes in reverse finishing order on the transposed graph
    visited.clear()
    sccs = []

    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs_transposed(node, visited, scc, transposed_graph)
            sccs.append(scc)

    return sccs


# Example graph represented as an adjacency list
graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [], 5: [6], 6: [5], 7: [6]}

sccs = kosaraju_scc(graph)

# Display the result
print("Strongly Connected Components:", sccs)
