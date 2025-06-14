def quick_sort(arr):
    """
    Performs Quick Sort on an array.

    Quick Sort is a divide-and-conquer algorithm that selects a pivot element, partitions the array
    into two subarrays (elements less than the pivot and elements greater than the pivot), and
    recursively sorts the subarrays.

    Time Complexity:
        - Best Case: O(n log n) -> When the pivot divides the array into roughly equal halves.
        - Average Case: O(n log n) -> Expected time complexity in most cases.
        - Worst Case: O(n^2) -> When the smallest or largest element is always chosen as the pivot (unbalanced partitions).

    Space Complexity:
        - O(log n) -> Recursive call stack in the best/average case.
        - O(n) -> In the worst case (unbalanced partitions leading to deep recursion).

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: A sorted version of the input list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Output: [1, 5, 7, 8, 9, 10]
