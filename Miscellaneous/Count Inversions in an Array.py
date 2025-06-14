def merge_and_count(arr, temp_arr, left, mid, right):
    """
    Merges two halves of the array and counts inversions.

    Args:
    arr (List[int]): Original array.
    temp_arr (List[int]): Temporary array for merging.
    left (int): Left index.
    mid (int): Mid index.
    right (int): Right index.

    Returns:
    int: Number of inversions in this merge step.
    """
    i = left  # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index for merged subarray
    inv_count = 0

    # Merge the two subarrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            # If an element from right is smaller, all remaining elements in left are inversions
            inv_count += mid - i + 1
            j += 1
        k += 1

    # Copy remaining elements of left subarray (if any)
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarray (if any)
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged temp array back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    """
    Recursively divides the array, sorts, and counts inversions.

    Args:
    arr (List[int]): Original array.
    temp_arr (List[int]): Temporary array for merging.
    left (int): Left index.
    right (int): Right index.

    Returns:
    int: Total number of inversions in the array.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def count_inversions(arr):
    """
    Wrapper function to count inversions in an array.

    Args:
    arr (List[int]): List of integers.

    Returns:
    int: Total number of inversions.

    Time Complexity: O(n log n) — due to merge sort.
    Space Complexity: O(n) — for the temporary array.
    """
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)


# Example usage:
arr = [1, 20, 6, 4, 5]
print("Number of inversions:", count_inversions(arr))
# Output: Number of inversions: 5
