def merge_sort(arr):
    """
    Performs Merge Sort on an array.

    Merge Sort is a divide-and-conquer algorithm that:
    1. Recursively divides the array into two halves.
    2. Sorts each half.
    3. Merges the sorted halves back together.

    Time Complexity:
        - Best Case: O(n log n) -> Always divides the array into equal halves.
        - Average Case: O(n log n) -> Consistently divides and merges.
        - Worst Case: O(n log n) -> Always requires merging.

    Space Complexity:
        - O(n) -> Temporary arrays are used for merging.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: A sorted version of the input list.
    """
    if len(arr) <= 1:
        return arr

    # Finding the middle of the array
    mid = len(arr) // 2

    # Recursively sorting both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merging the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Time Complexity: O(n), where n is the total number of elements in both lists.
    Space Complexity: O(n), as it requires additional space for the merged list.

    Parameters:
        left (list): Sorted left half.
        right (list): Sorted right half.

    Returns:
        list: Merged sorted list.
    """
    sorted_arr = []
    i = j = 0

    # Merging elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Adding remaining elements, if any
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [5, 6, 7, 11, 12, 13]
