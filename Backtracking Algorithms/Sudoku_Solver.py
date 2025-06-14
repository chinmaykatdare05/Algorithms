def is_valid(board, row, col, num):
    """
    Check if placing 'num' at board[row][col] is valid under Sudoku rules.

    Time Complexity: O(9) = O(1) (Checking row, column, and 3x3 box)
    """
    # Check the row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using Backtracking.

    Time Complexity: O(9^(N)), where N is the number of empty cells.
    Space Complexity: O(1) (In-place modification of board)
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":  # Empty cell found
                for num in "123456789":  # Try placing digits 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place number
                        if solve_sudoku(board):  # Recursive call
                            return True
                        board[row][col] = "."  # Backtrack if not solvable

                return False  # No valid number found, trigger backtracking

    return True  # Puzzle solved


def print_sudoku(board):
    """Helper function to print Sudoku board."""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        print(
            " ".join(row[:3]) + " | " + " ".join(row[3:6]) + " | " + " ".join(row[6:])
        )


# Example Usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print("Sudoku Puzzle:")
print_sudoku(sudoku_board)
solve_sudoku(sudoku_board)
print("\nSolved Sudoku:")
print_sudoku(sudoku_board)
