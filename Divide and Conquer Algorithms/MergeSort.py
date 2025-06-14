def merge_sort(arr):
    """
    Sorts an array using Merge Sort algorithm.

    Time Complexity:
        - Best Case: O(N log N)
        - Average Case: O(N log N)
        - Worst Case: O(N log N)

    Space Complexity: O(N) (Extra space for temporary arrays)

    Args:
        arr (List[int]): The list to be sorted.

    Returns:
        List[int]: Sorted list.
    """
    if len(arr) <= 1:
        return arr  # Base case: Already sorted

    # Split array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Time Complexity: O(N) where N is len(left) + len(right).
    Space Complexity: O(N) (Temporary array).

    Args:
        left (List[int]): Left half (sorted).
        right (List[int]): Right half (sorted).

    Returns:
        List[int]: Merged sorted list.
    """
    merged = []
    i = j = 0

    # Merge the two lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
