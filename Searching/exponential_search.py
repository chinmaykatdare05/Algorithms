def binary_search(arr, left, right, target):
    """
    Performs Binary Search on a sorted array.

    Time Complexity: O(log n)
    Space Complexity: O(1) (Iterative implementation)

    Parameters:
        arr (list): Sorted list of elements.
        left (int): Left index of the search range.
        right (int): Right index of the search range.
        target (int/float): Element to search for.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    """
    Performs Exponential Search on a sorted array.

    Exponential Search works by doubling the search range until it finds
    a suitable boundary and then applying Binary Search.

    Time Complexity:
        - Best Case: O(1) (If target is at index 0)
        - Average/Worst Case: O(log n) (Same as Binary Search)

    Space Complexity:
        - O(1) (Uses constant extra space)

    Parameters:
        arr (list): Sorted list of elements.
        target (int/float): Element to search for.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    if arr[0] == target:
        return 0  # If target is at the first position

    n = len(arr)
    index = 1

    while index < n and arr[index] <= target:
        index *= 2  # Exponentially increase the index

    # Perform binary search in the identified range
    return binary_search(arr, index // 2, min(index, n - 1), target)


# Example usage
arr = [2, 3, 4, 10, 15, 20, 25, 30, 40, 50]
target = 15
print("Exponential Search Result:", exponential_search(arr, target))  # Output: 4
