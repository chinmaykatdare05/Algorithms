def heap_sort(arr):
    """
    Performs Heap Sort on an array.

    Heap Sort is a comparison-based sorting algorithm that first transforms the input
    array into a max heap and then repeatedly extracts the maximum element from the heap
    to build a sorted array.

    Time Complexity:
        - Best Case: O(n log n) -> Always maintains heap properties.
        - Average Case: O(n log n) -> Heapify and extraction take log n time each.
        - Worst Case: O(n log n) -> Even in reverse-sorted input, heap operations take log n.

    Space Complexity:
        - O(1) -> Sorting is done in place without extra memory.

    Parameters:
        arr (list): The list of numbers to be sorted.

    Returns:
        list: The sorted list (sorted in place).
    """

    def heapify(arr, n, i):
        """
        Maintains the max heap property for a subtree rooted at index i.

        Time Complexity: O(log n), as it may traverse the height of the heap.

        Parameters:
            arr (list): The list representing the heap.
            n (int): Size of the heap.
            i (int): Index of the root node of the subtree.
        """
        largest = i  # Initialize the largest as root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build a max heap (heapify non-leaf nodes from bottom up)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with last element
        heapify(arr, i, 0)  # Restore heap property on reduced heap

    return arr


# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(sorted_arr)  # Output: [5, 6, 7, 11, 12, 13]
