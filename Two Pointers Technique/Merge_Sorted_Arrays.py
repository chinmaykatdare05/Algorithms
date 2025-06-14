def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays into one sorted array.

    Time Complexity: O(n + m)
    - n: Length of arr1
    - m: Length of arr2
    - Each element is processed once, making this linear.

    Space Complexity: O(n + m)
    - A new array is created to hold all elements from both arrays.

    Args:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.

    Returns:
    list: A merged sorted array.
    """
    i, j = 0, 0
    merged = []

    # Merge arrays by comparing elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements from arr1 or arr2
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


# Test case
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print("Merged Array:", merge_sorted_arrays(arr1, arr2))
