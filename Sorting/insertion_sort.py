def insertion_sort(arr):
    """
    Performs Insertion Sort on an array.

    Insertion Sort builds the sorted array one element at a time by picking the next
    element and inserting it into its correct position in the sorted part of the array.

    Time Complexity:
        - Best Case: O(n) -> When the array is already sorted (only comparisons are made).
        - Average Case: O(n^2) -> Due to nested loops.
        - Worst Case: O(n^2) -> When the array is sorted in reverse order.

    Space Complexity:
        - O(1) -> Sorting is done in place without extra memory.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list (sorted in place).
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Element to be inserted
        j = i - 1
        while j >= 0 and arr[j] > key:  # Shift elements to make space for the key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert key into its correct position
    return arr


# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [5, 6, 11, 12, 13]
