def radix_sort(arr):
    """
    Performs Radix Sort on an array.

    Radix Sort is a non-comparison-based sorting algorithm that sorts numbers by processing
    individual digits from the least significant to the most significant, using Counting Sort
    as a subroutine.

    This algorithm is efficient for integers with a limited number of digits.

    Time Complexity:
        - Best Case: O(nk) -> Where n is the number of elements and k is the number of digits.
        - Average Case: O(nk) -> Consistent performance for fixed-digit numbers.
        - Worst Case: O(nk) -> Linear time if k is small.

    Space Complexity:
        - O(n + k) -> Extra space for counting sort.

    Parameters:
        arr (list): The list of non-negative integers to be sorted.

    Returns:
        list: The sorted list.
    """
    if not arr:
        return []

    # Get the maximum number to determine the number of digits
    max_val = max(arr)
    exp = 1  # Start with the least significant digit

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10  # Move to the next significant digit

    return arr


def counting_sort_by_digit(arr, exp):
    """
    A stable version of Counting Sort used as a subroutine for Radix Sort.

    Time Complexity: O(n), where n is the length of the array.
    Space Complexity: O(n), since we use additional arrays.

    Parameters:
        arr (list): The list of numbers to be sorted by a specific digit.
        exp (int): The exponent representing the digit place being sorted (1s, 10s, 100s, etc.).
    """
    n = len(arr)
    output = [0] * n  # Output array to store sorted values
    count = [0] * 10  # Count array for digit occurrences (0-9)

    # Count occurrences of each digit at the current place value
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Compute cumulative count to maintain stability
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in a stable manner
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the sorted values back to the original array
    for i in range(n):
        arr[i] = output[i]


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
