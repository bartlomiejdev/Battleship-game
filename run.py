import random

# Function to print the board


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

# Function to randomly place the ships on the board


def place_ships(board):
    ship_size = 4
    for _ in range(ship_size):
        # Generate random coordinates for the ship
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        # Check if the coordinates are already occupied by a ship
        while board[ship_row][ship_col] == "O":
            ship_row = random.randint(0, len(board) - 1)
            ship_col = random.randint(0, len(board[0]) - 1)
        # Place the ship on the board
        board[ship_row][ship_col] = "O"

# Function to check if the user's guess is a hit or miss


def check_guess(guess, board):
    row, col = guess
    if board[row][col] == "O":
        board[row][col] = "X"
        return True
    else:
        board[row][col] = "M"
        return False
