def quick_sort(arr, low, high):
    """
    Sorts an array using Quick Sort algorithm (Lomuto Partition).

    Time Complexity:
        - Best Case: O(N log N)
        - Average Case: O(N log N)
        - Worst Case: O(N²) (If the pivot selection is poor)

    Space Complexity: O(log N) (Recursive call stack)

    Args:
        arr (List[int]): The list to be sorted.
        low (int): Starting index.
        high (int): Ending index.

    Returns:
        None (Sorts in place).
    """
    if low < high:
        pivot_index = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pivot_index - 1)  # Sort left half
        quick_sort(arr, pivot_index + 1, high)  # Sort right half


def partition(arr, low, high):
    """
    Partitions the array using the last element as pivot.

    Time Complexity: O(N) (Iterating once through the array).
    Space Complexity: O(1) (In-place swapping).

    Args:
        arr (List[int]): The list to partition.
        low (int): Starting index.
        high (int): Ending index (pivot element).

    Returns:
        int: The final index of the pivot.
    """
    pivot = arr[high]  # Select last element as pivot
    i = low - 1  # Pointer for smaller element

    for j in range(low, high):
        if arr[j] < pivot:  # Move smaller elements to the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot correctly
    return i + 1  # Return pivot index


# Example Usage
arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
