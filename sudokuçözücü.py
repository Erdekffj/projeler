def find_empty(board):
    """
    Finds an empty cell in the board and returns its coordinates
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    """
    Checks whether placing the given number at the given position is a valid move
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    """
    Solves the given Sudoku board using backtracking and recursion
    """
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# Example board
board = [
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [5, 1, 0, 4, 2, 0, 6, 0, 0],
    [0, 8, 0, 3, 0, 0, 7, 0, 0],
    [0, 0, 8, 0, 0, 1, 3, 7, 0],
    [0, 2, 3, 0, 8, 0, 0, 4, 0],
    [4, 0, 0, 9, 0, 0, 1, 0, 0],
    [9, 6, 2, 8, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 1, 0, 4, 0, 0],
    [7, 0, 0, 2, 0, 3, 0, 9, 6]
]

# Solve the board
if solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
else:
    print("No solution exists.")
