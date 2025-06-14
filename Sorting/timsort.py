def insertion_sort(arr, left, right):
    """
    Performs Insertion Sort on a portion of the array.

    Time Complexity: O(n^2) in the worst case.
    Space Complexity: O(1) as it sorts in place.

    Parameters:
        arr (list): The list to be sorted.
        left (int): Starting index of the subarray.
        right (int): Ending index of the subarray.
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays of `arr`.

    Time Complexity: O(n)
    Space Complexity: O(n) due to temporary arrays.

    Parameters:
        arr (list): The main array containing two sorted subarrays.
        left (int): Starting index of the first sorted subarray.
        mid (int): Ending index of the first sorted subarray.
        right (int): Ending index of the second sorted subarray.
    """
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = arr[left : mid + 1], arr[mid + 1 : right + 1]

    i = j = 0
    k = left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1


def timsort(arr):
    """
    Performs Timsort on an array.

    Timsort divides the array into small chunks (RUN size), sorts them using Insertion Sort,
    and then merges them using Merge Sort.

    Time Complexity:
        - Best Case: O(n) -> Already sorted array (only insertion sort is needed).
        - Average Case: O(n log n) -> Efficient hybrid approach.
        - Worst Case: O(n log n) -> Follows Merge Sort’s complexity.

    Space Complexity:
        - O(n) -> Due to merge operations.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    RUN = 32  # Default run size used in Python's implementation

    # Sort individual subarrays of size RUN using Insertion Sort
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min((i + RUN - 1), n - 1))

    # Merge sorted subarrays
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr


# Example usage
arr = [5, 21, 7, 23, 19, 1, 18, 12]
sorted_arr = timsort(arr)
print(sorted_arr)  # Output: [1, 5, 7, 12, 18, 19, 21, 23]
