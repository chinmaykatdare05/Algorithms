def shell_sort(arr):
    """
    Performs Shell Sort on an array.

    Shell Sort is an optimization of Insertion Sort that reduces the number of shifts
    by allowing elements to be swapped at a larger gap before performing the final
    Insertion Sort.

    Time Complexity:
        - Best Case: O(n log n) -> Depends on the gap sequence.
        - Average Case: O(n^(3/2)) -> Common complexity for practical gap sequences.
        - Worst Case: O(n^2) -> When using poor gap sequences.

    Space Complexity:
        - O(1) -> Sorting is done in place.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    gap = n // 2  # Start with an initial gap (Knuth sequence can be used)

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap

    return arr


# Example usage
arr = [12, 34, 54, 2, 3]
sorted_arr = shell_sort(arr)
print(sorted_arr)  # Output: [2, 3, 12, 34, 54]
