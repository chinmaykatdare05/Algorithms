def is_safe(board, row, col, n):
    """
    Checks if a queen can be placed at board[row][col] without conflicts.

    Time Complexity: O(N) per placement check
    """
    # Check the column (above rows)
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n, solutions):
    """
    Solves the N-Queens problem using backtracking and stores valid solutions.

    Time Complexity: O(N!)
    Space Complexity: O(N^2) (Can be optimized to O(N))
    """
    if row == n:  # All queens placed
        solutions.append(["".join(r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"  # Place queen
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = "."  # Backtrack (Remove queen)


def n_queens(n):
    """
    Returns all possible solutions for N-Queens problem.

    Time Complexity: O(N!)
    """
    board = [["."] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions


# Example Usage
n = 4  # Change N to test different sizes
solutions = n_queens(n)
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
