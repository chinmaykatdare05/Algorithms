def counting_sort(arr):
    """
    Performs Counting Sort on an array.

    Counting Sort is a non-comparison-based sorting algorithm that sorts integers
    by counting occurrences and using prefix sums to place elements in the correct position.

    This algorithm is efficient when sorting integers within a limited range [0, k].

    Time Complexity:
        - Best Case: O(n + k) -> Always processes n elements and k unique values.
        - Average Case: O(n + k) -> Consistently linear when k is small.
        - Worst Case: O(n + k) -> Performance degrades if k (range of numbers) is large.

    Space Complexity:
        - O(k) -> Extra space for the count array.

    Parameters:
        arr (list): The list of non-negative integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if not arr:
        return []

    # Find the maximum value in the array
    max_val = max(arr)

    # Initialize the count array
    count = [0] * (max_val + 1)

    # Store the count of each element
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)

    return sorted_arr


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # Output: [1, 2, 2, 3, 3, 4, 8]
