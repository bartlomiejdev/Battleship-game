def print_board(board):
    print("  ", end="")
    for i in enumerate(board[0]):
        print(str(i+1), end=" ")
    print()
    for i, row in enumerate(board):
        row_str = str(i + 1) + " "
        for cell in row:
            if cell == ".":
                row_str += ". "
            else:
                row_str += cell + " "
        print(row_str)
