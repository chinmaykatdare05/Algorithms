import math


def euclidean_distance(p1, p2):
    """Computes the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force_closest_pair(points):
    """Finds the closest pair using brute-force approach (O(N^2))."""
    min_dist = float("inf")
    n = len(points)
    closest_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return min_dist, closest_pair


def closest_split_pair(points_sorted_by_y, min_dist, best_pair):
    """Checks points near the middle strip for closer pairs."""
    n = len(points_sorted_by_y)
    for i in range(n):
        for j in range(
            i + 1, min(i + 7, n)
        ):  # Check only 6 neighbors (theoretical proof)
            dist = euclidean_distance(points_sorted_by_y[i], points_sorted_by_y[j])
            if dist < min_dist:
                min_dist = dist
                best_pair = (points_sorted_by_y[i], points_sorted_by_y[j])

    return min_dist, best_pair


def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    """Recursively finds the closest pair of points (O(N log N))."""
    n = len(points_sorted_by_x)

    # Base case: Use brute force for small subsets
    if n <= 3:
        return brute_force_closest_pair(points_sorted_by_x)

    mid = n // 2
    left_x = points_sorted_by_x[:mid]
    right_x = points_sorted_by_x[mid:]

    midpoint = points_sorted_by_x[mid][0]
    left_y = list(filter(lambda p: p[0] <= midpoint, points_sorted_by_y))
    right_y = list(filter(lambda p: p[0] > midpoint, points_sorted_by_y))

    # Recursively find closest pairs in left and right halves
    min_dist_left, pair_left = closest_pair_recursive(left_x, left_y)
    min_dist_right, pair_right = closest_pair_recursive(right_x, right_y)

    # Get the best result from left and right
    if min_dist_left < min_dist_right:
        min_dist = min_dist_left
        best_pair = pair_left
    else:
        min_dist = min_dist_right
        best_pair = pair_right

    # Find closest pair crossing the midpoint
    min_dist_split, pair_split = closest_split_pair(
        points_sorted_by_y, min_dist, best_pair
    )

    if min_dist_split < min_dist:
        return min_dist_split, pair_split
    else:
        return min_dist, best_pair


def closest_pair(points):
    """
    Finds the closest pair of points using Divide & Conquer approach.

    Time Complexity: O(N log N) (Sorting + Recursive calls)
    Space Complexity: O(N) (Storing sorted lists and recursive calls)

    Args:
        points (List[Tuple[int, int]]): List of (x, y) points.

    Returns:
        Tuple[float, Tuple[Tuple[int, int], Tuple[int, int]]]:
        Minimum distance and closest pair of points.
    """
    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)


# Example Usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_distance, closest_points = closest_pair(points)

print(f"Closest Pair: {closest_points}, Distance: {min_distance:.4f}")
