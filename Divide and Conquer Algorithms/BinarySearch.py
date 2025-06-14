def binary_search_iterative(arr, target):
    """
    Performs binary search on a sorted array (Iterative method).

    Time Complexity:
        - Best Case: O(1) (If the middle element is the target)
        - Average & Worst Case: O(log N) (Dividing the search space by half)

    Space Complexity: O(1) (No extra space used)

    Args:
        arr (List[int]): Sorted list of elements.
        target (int): Element to search for.

    Returns:
        int: Index of the target element, or -1 if not found.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index

        if arr[mid] == target:
            return mid  # Found the target
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found


# Example Usage
arr = [1, 3, 5, 7, 9, 11, 15]
target = 7
print("Element found at index:", binary_search_iterative(arr, target))


def binary_search_recursive(arr, low, high, target):
    """
    Performs binary search on a sorted array (Recursive method).

    Time Complexity: O(log N)
    Space Complexity: O(log N) (Recursive call stack)

    Args:
        arr (List[int]): Sorted list of elements.
        low (int): Starting index.
        high (int): Ending index.
        target (int): Element to search for.

    Returns:
        int: Index of the target element, or -1 if not found.
    """
    if low > high:
        return -1  # Base case: Element not found

    mid = (low + high) // 2  # Find middle index

    if arr[mid] == target:
        return mid  # Found the target
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)  # Search right half
    else:
        return binary_search_recursive(arr, low, mid - 1, target)  # Search left half


# Example Usage
arr = [1, 3, 5, 7, 9, 11, 15]
target = 7
print("Element found at index:", binary_search_recursive(arr, 0, len(arr) - 1, target))
