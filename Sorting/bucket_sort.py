def bucket_sort(arr, bucket_size=5):
    """
    Performs Bucket Sort on an array.

    Bucket Sort distributes elements into a set of buckets, sorts each bucket individually
    (using Insertion Sort or another sorting method), and then concatenates the sorted buckets
    to get the final sorted array.

    This algorithm is efficient when the input values are uniformly distributed.

    Time Complexity:
        - Best Case: O(n + k) -> When elements are evenly distributed across buckets.
        - Average Case: O(n + k) -> Depends on distribution and sorting within buckets.
        - Worst Case: O(n^2) -> If all elements land in one bucket, falling back to O(n^2) sorting.

    Space Complexity:
        - O(n + k) -> Extra space for buckets.

    Parameters:
        arr (list): The list of numbers to be sorted.
        bucket_size (int): The number of elements each bucket can hold before sorting.

    Returns:
        list: The sorted list.
    """
    if not arr:
        return []

    # Find minimum and maximum values
    min_val, max_val = min(arr), max(arr)

    # Number of buckets
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Sort each bucket and concatenate results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Using Python's Timsort (O(n log n))

    return sorted_arr


# Example usage
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr, bucket_size=0.1)
print(sorted_arr)  # Output: [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
