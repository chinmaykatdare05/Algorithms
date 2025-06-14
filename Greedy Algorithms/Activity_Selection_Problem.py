def max_activities(start, end):
    """
    Selects the maximum number of non-overlapping activities.

    Time Complexity: O(N log N)  (due to sorting)
    Space Complexity: O(1)
    """
    # Combine start and end times and sort by end time
    activities = sorted(zip(start, end), key=lambda x: x[1])

    count = 0
    last_end_time = 0

    for s, e in activities:
        if s >= last_end_time:
            count += 1
            last_end_time = e  # Update the last selected activity's end time

    return count


# Example Usage
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print(max_activities(start_times, end_times))  # Output: 4
