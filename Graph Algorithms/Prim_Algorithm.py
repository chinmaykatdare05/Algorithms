import heapq


def prim(graph, start=0):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST)
    of a weighted, undirected graph using a priority queue (min-heap).

    Time Complexity: O((V + E) * log(V))
        - V: Number of nodes
        - E: Number of edges
        - Each edge gets pushed/popped from the heap, costing log(V) time.

    Space Complexity: O(V + E)
        - V: To track visited nodes
        - E: To store all edges in the heap

    Args:
        graph (dict): Adjacency list where each node maps to a list of tuples (neighbor, weight).
        start (int): Starting node (default is node 0).

    Returns:
        list: Edges included in the MST and the total weight.
    """
    visited = set()
    mst = []  # Store edges in the MST
    total_weight = 0
    min_heap = [(0, start, -1)]  # (weight, node, parent)

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_weight += weight

            # If the node has a parent, record the edge
            if parent != -1:
                mst.append((parent, node, weight))

            # Add all neighboring nodes to the heap
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))

    # Return MST edges and total weight
    return mst, total_weight


# Example graph represented as an adjacency list
graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 3), (3, 2)],
    2: [(0, 4), (1, 3), (3, 5)],
    3: [(1, 2), (2, 5)],
}

mst, total_weight = prim(graph)
print("Minimum Spanning Tree Edges:", mst)
print("Total Weight:", total_weight)
