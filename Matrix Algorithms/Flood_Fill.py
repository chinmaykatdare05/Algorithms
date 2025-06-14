def flood_fill(image, sr, sc, new_color):
    """
    Performs a flood fill on an image starting from a given pixel.

    Time Complexity: O(m * n)
    - Each pixel is visited once.

    Space Complexity: O(m * n)
    - Due to the recursion stack or queue for BFS.

    Args:
        image (list of lists): 2D grid representing the image.
        sr (int): Starting row.
        sc (int): Starting column.
        new_color (int): The color to fill with.

    Returns:
        list of lists: Modified image after flood fill.
    """
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # If the starting pixel is already the new color, no need to proceed
    if original_color == new_color:
        return image

    # Directions: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c):
        # Base case: if out of bounds or different color
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return

        # Fill the current cell with new color
        image[r][c] = new_color

        # Recursively apply flood fill in all directions
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Start flood fill from the initial pixel
    dfs(sr, sc)

    return image


# Test case
image = [[1, 1, 0], [1, 1, 0], [0, 0, 2]]

start_row, start_col = 0, 0
new_color = 3

result = flood_fill(image, start_row, start_col, new_color)

# Output the result
for row in result:
    print(row)
