def max_non_overlapping_intervals(intervals):
    """
    Finds the maximum number of non-overlapping intervals.

    Time Complexity: O(N log N)  (Sorting dominates)
    Space Complexity: O(1)
    """
    # Sort intervals by their ending times
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end_time = float("-inf")

    for start, end in intervals:
        if start >= last_end_time:
            count += 1
            last_end_time = end  # Update the last selected interval's end time

    return count


# Example Usage
intervals = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 10)]
print(max_non_overlapping_intervals(intervals))  # Output: 3
