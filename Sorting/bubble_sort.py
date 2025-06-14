def bubble_sort(arr):
    """
    Performs Bubble Sort on an array.

    Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated
    until the list is sorted.

    Time Complexity:
        - Best Case: O(n) -> When the array is already sorted (with an optimization check).
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
    for i in range(n):
        swapped = False  # Optimization: Check if a swap happened
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if the element is greater than the next one
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps were made, the array is already sorted
            break
    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
