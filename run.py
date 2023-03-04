def print_board(board):
    print("  ", end="")
    for i in range(len(board[0])):
        print(str(i+1), end=" ")
    print()
    for i in range(len(board)):
        row_str = str(i + 1) + " "
        for j in range(len(board[i])):
            if board[i][j] == ".":
                row_str += ". "
            else:
                row_str += board[i][j] + " "
        print(row_str)