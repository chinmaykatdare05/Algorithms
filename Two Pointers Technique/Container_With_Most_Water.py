def max_area(height):
    """
    Finds the maximum water container area between two lines.

    Time Complexity: O(n)
    - n: Number of elements in the height array.
    - Each line is processed once by moving the pointers.

    Space Complexity: O(1)
    - Only a few variables are stored, no extra space used.

    Args:
    height (list): List of non-negative integers representing the heights.

    Returns:
    int: The maximum area that can hold water.
    """
    left, right = 0, len(height) - 1
    max_water = 0

    # Two-pointer approach
    while left < right:
        # Calculate the current area and update max area
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)

        # Move the pointer corresponding to the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Test case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Max Water:", max_area(height))
