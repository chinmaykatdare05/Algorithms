def linear_search(arr, target):
    """
    Performs Linear Search iteratively.

    Linear Search scans each element of the array one by one until it finds the target.

    Time Complexity:
        - Best Case: O(1) -> Target found at the first position.
        - Average Case: O(n) -> On average, checks half the elements.
        - Worst Case: O(n) -> When the target is at the end or not present.

    Space Complexity:
        - O(1) -> No extra space used.

    Parameters:
        arr (list): The list of elements.
        target (int or float): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found
    return -1  # Target not found


# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
print(linear_search(arr, target))  # Output: 2
