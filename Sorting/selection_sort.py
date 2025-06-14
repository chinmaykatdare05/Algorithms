def selection_sort(arr):
    """
    Performs Selection Sort on an array.

    Selection Sort is an in-place sorting algorithm that divides the array into two parts:
    the sorted part and the unsorted part. It repeatedly finds the smallest element in the
    unsorted part and swaps it with the leftmost unsorted element.

    Time Complexity:
        - Best Case: O(n^2) -> Still requires scanning the entire list for the smallest element.
        - Average Case: O(n^2) -> Due to the nested loops.
        - Worst Case: O(n^2) -> Even if the array is sorted in reverse order, it performs the same number of operations.

    Space Complexity:
        - O(1) -> Sorting is done in place without extra memory.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list (sorted in place).
    """
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current element is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the minimum element
                min_index = j
        arr[i], arr[min_index] = (
            arr[min_index],
            arr[i],
        )  # Swap the found minimum with the first unsorted element
    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]
