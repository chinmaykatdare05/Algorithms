def exist(board, word):
    """
    Checks if a given word exists in a 2D board using backtracking.

    Time Complexity: O(m * n * 4^L) - where m, n are board dimensions, and L is the word length.
    Space Complexity: O(L) - recursive depth stack.

    Args:
        board (List[List[str]]): The 2D grid of characters.
        word (str): The target word to search.

    Returns:
        bool: True if the word exists, False otherwise.
    """

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # Base case: entire word is found
        if index == len(word):
            return True

        # Boundary check and character match
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        # Temporarily mark the cell as visited
        temp, board[r][c] = board[r][c], "#"

        # Explore all four possible directions (up, down, left, right)
        found = (
            dfs(r + 1, c, index + 1)  # Down
            or dfs(r - 1, c, index + 1)  # Up
            or dfs(r, c + 1, index + 1)  # Right
            or dfs(r, c - 1, index + 1)
        )  # Left

        # Restore the original value (backtracking)
        board[r][c] = temp

        return found

    # Start DFS from every cell in the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False


# Example Usage
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCCED"  # True
word2 = "SEE"  # True
word3 = "ABCB"  # False

print(exist(board, word1))  # Output: True
print(exist(board, word2))  # Output: True
print(exist(board, word3))  # Output: False
