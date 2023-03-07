'''Importing libs'''
import random
import os


def get_user_name():
    '''Function to get user name and return it'''
    name = input("What is your name? ")
    print(f"Hello {name}! Let's play Battleship.\n")
    return name


def print_board(board, hide_ships=True):
    '''Function to print out the board with parameter to hide opponents ship'''
    print("  ", end="")
    for i, _ in enumerate(board[0]):
        print(str(i+1), end=" ")
    print()
    for i, row in enumerate(board):
        row_str = str(i + 1) + " "
        for cell in row:
            if hide_ships and cell == "O":
                row_str += ". "
            else:
                row_str += cell + " "
        print(row_str)


def place_ships(board, board_size):
    '''Function that place the ships on the board'''
    ship_size = board_size - 1
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


def check_guess(guess, board):
    '''Function to check if the user's guess is a hit or miss'''
    row, col = guess
    if board[row][col] == "O":
        board[row][col] = "X"
        return True
    else:
        board[row][col] = "M"
        return False


def grid_size():
    '''Function to set up the board size based on user input'''
    while True:
        board_size_user_choice = input("Choose size of grid from 1-9: \n")
        if (board_size_user_choice.isdigit() and
                1 <= int(board_size_user_choice)) <= 9:
            board_size_user_choice = int(board_size_user_choice)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def set_up_player_board(grid_size):
    '''Set ups the player board as a list based on the value returned from grid_size()'''
    # Set up players board
    board_size = grid_size
    player_board = []
    for _ in range(board_size):
        player_board.append(["."] * board_size)
    place_ships(player_board, board_size)
    return player_board


def set_up_computer_board(grid_size):
    '''Set ups the computer board as a list based on the value returned from grid_size()'''
    # Set up computer board
    board_size = grid_size
    computer_board = []
    for _ in range(board_size):
        computer_board.append(["."] * board_size)
    place_ships(computer_board, board_size)
    return computer_board


def update_ship_count(board):
    '''Ship count function to check how many "O" is there in the board'''
    ship_count = 0
    for row in board:
        for cell in row:
            if cell == "O":
                ship_count += 1
    return ship_count


def game_loop(grid_size, name):
    '''Game loop function that takes two parameters to run player and
    computer turns, sets the ships counts for the player and computer and sets
    up the boards by calling the functions'''
    board_size = grid_size
    computer_ships = board_size - 1
    player_ships = board_size - 1
    player_board = set_up_player_board(board_size)
    computer_board = set_up_computer_board(board_size)

    while computer_ships > 0 and player_ships > 0:
        # Print the board after each round

        print("\nThis is your board:")
        print_board(player_board, False)
        print("\nThis is computer's board:")
        print_board(computer_board, True)

        # Update ship counts

        computer_ships = update_ship_count(computer_board)
        player_ships = update_ship_count(player_board)
        ships = [player_ships, computer_ships]
        player_turn(board_size, computer_board, name, ships)
        computer_turn(board_size, player_board, ships)

    return (player_ships, computer_ships)


def player_turn(board_size, computer_board, name, ships):
    '''Player turn function that ask user for row and column
    validate the input and check if the player hit the target or/and
     win the game'''
    print("\nYour turn.")
    ships = list(ships)
    while True:
        guess_row = input(f"Guess Row (1-{board_size}): ")
        guess_col = input(f"Guess Col (1-{board_size}): ")

        if not guess_row.isdigit() or not guess_col.isdigit():
            print("Please enter a valid integer.")
            continue

        guess_row = int(guess_row) - 1
        guess_col = int(guess_col) - 1
        if (guess_row < 0 or guess_row >= board_size or
                guess_col < 0 or guess_col >= board_size):
            print(f"Please enter integers in the range 1-{board_size}.")
            continue
        break

    guess = (guess_row, guess_col)
    if check_guess(guess, computer_board):
        ships[1] -= 1
        print("Congratulations! You sunk a battleship!")
        if ships[1] == 0:
            print(f"\nCongratulations, {name}! You won!")
            # break
            # FIX THE ISSUE WITH QUITING GAME
    else:
        print("You missed.")


def clear_console():
    '''Clearing the console'''
    os.system('cls')


# def main():
#     '''Function that ask for name, sets up
#      the boards, lopping game and set the turns'''
#     # Get the user's name

#     while True:
#         board_size_user_choice = input("Choose size of grid from 1-9: \n")
#         if (board_size_user_choice.isdigit() and
#                 1 <= int(board_size_user_choice)) <= 9:
#             board_size_user_choice = int(board_size_user_choice)
#             break
#         else:
#             print("Invalid input. Please enter a number between 1 and 9.")

#     # Set up players board
#     board_size = board_size_user_choice
#     player_board = []
#     for _ in range(board_size):
#         player_board.append(["."] * board_size)
#     place_ships(player_board, board_size)

#     # Set up computers board
#     computer_board = []
#     for _ in range(board_size):
#         computer_board.append(["."] * board_size)
#     place_ships(computer_board, board_size)

#     # Game loop
#     computer_ships = board_size - 1
#     player_ships = board_size - 1
#     while computer_ships > 0 and player_ships > 0:

#         # Print the board after each round
#         print("\nThis is your board:")
#         print_board(player_board, False)
#         print("\nThis is computer's board:")
#         print_board(computer_board, True)

#         # User's turn
#         print("\nYour turn.")
#         while True:
#             guess_row = input(f"Guess Row (1-{board_size}): ")
#             guess_col = input(f"Guess Col (1-{board_size}): ")

#             if not guess_row.isdigit() or not guess_col.isdigit():
#                 print("Please enter a valid integer.")
#                 continue
#             guess_row = int(guess_row) - 1
#             guess_col = int(guess_col) - 1
#             if (guess_row < 0 or guess_row >= board_size or
#                     guess_col < 0 or guess_col >= board_size):
#                 print(f"Please enter integers in the range 1-{board_size}.")
#                 continue
#             break

#         guess = (guess_row, guess_col)
#         if check_guess(guess, computer_board):
#             computer_ships -= 1
#             print("Congratulations! You sunk a battleship!")
#             if computer_ships == 0:
#                 print(f"\nCongratulations, {name}! You won!")
#                 break
#         else:
#             print("You missed.")

#         # Computer turn
#         print("\nComputer's turn.")
#         while True:
#             comp_guess_row = random.randint(0, board_size - 1)
#             comp_guess_col = random.randint(0, board_size - 1)
#             comp_guess = (comp_guess_row, comp_guess_col)
#             if (player_board[comp_guess_row][comp_guess_col] != "M" and
#                     player_board[comp_guess_row][comp_guess_col] != "X"):
#                 break
#         if check_guess(comp_guess, player_board):
#             player_ships -= 1
#             print("Oh no! The computer sunk one of your battleships!")
#             if player_ships == 0:
#                 print("Computer hit your last ship! You lose!")
#         else:
#             print("The computer missed.")

#     # Print the final board
#     print("\nThis is your final board:\n")
#     print_board(player_board, False)
#     print("\nThis is computer final board:\n")
#     print_board(computer_board, False)


if __name__ == "__main__":
    main()
