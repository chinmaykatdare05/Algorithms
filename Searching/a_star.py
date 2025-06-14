import heapq


def astar(graph, start, goal, heuristic):
    """
    Performs the A* search algorithm to find the shortest path.

    A* uses both actual cost (g) and estimated cost (h) to find the optimal path.

    Time Complexity:
        - O(E log V) (Similar to Dijkstra’s algorithm but depends on heuristic efficiency).

    Space Complexity:
        - O(V) (Stores all nodes in priority queue and path dictionary).

    Parameters:
        graph (dict): Adjacency list where keys are nodes, values are lists of (neighbor, cost).
        start (str/int): The starting node.
        goal (str/int): The goal node.
        heuristic (dict): Estimated heuristic costs from each node to the goal.

    Returns:
        list: The shortest path from start to goal.
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (f(n), node)

    g_costs = {node: float("inf") for node in graph}
    g_costs[start] = 0

    came_from = {}  # Stores path history

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for neighbor, cost in graph[current]:
            tentative_g_cost = g_costs[current] + cost
            if tentative_g_cost < g_costs[neighbor]:  # Found a better path
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor))
                came_from[neighbor] = current

    return None  # No path found


# Example usage
graph = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}

heuristic = {"A": 7, "B": 3, "C": 2, "D": 0}  # Estimated heuristic distance to goal 'D'

print("A* Shortest Path:")
print(astar(graph, "A", "D", heuristic))  # Output: ['A', 'B', 'C', 'D']
