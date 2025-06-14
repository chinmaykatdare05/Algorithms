def binary_search_iterative(arr, target):
    """
    Performs Binary Search iteratively.

    Binary Search works by repeatedly dividing the search range in half.

    Time Complexity:
        - Best Case: O(1) -> When the target is found at the middle.
        - Average Case: O(log n) -> Reduces search space by half each iteration.
        - Worst Case: O(log n) -> If the target is at the extreme ends.

    Space Complexity:
        - O(1) -> Only uses constant space.

    Parameters:
        arr (list): The sorted list of elements.
        target (int or float): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents integer overflow
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search_iterative(arr, target))  # Output: 3


def binary_search_recursive(arr, target, left, right):
    """
    Performs Binary Search recursively.

    Recursively divides the search range in half to find the target.

    Time Complexity:
        - Best Case: O(1) -> When the target is found at the middle.
        - Average Case: O(log n) -> Reduces search space by half each recursion.
        - Worst Case: O(log n) -> If the target is at the extreme ends.

    Space Complexity:
        - O(log n) -> Due to recursive call stack.

    Parameters:
        arr (list): The sorted list of elements.
        target (int or float): The element to search for.
        left (int): The starting index of the search space.
        right (int): The ending index of the search space.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    if left > right:
        return -1  # Base case: target not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Search right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Search left half


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search_recursive(arr, target, 0, len(arr) - 1))  # Output: 3
