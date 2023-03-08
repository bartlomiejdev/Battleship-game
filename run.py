'''Importing libs'''
import random
import os


def get_user_name():
    '''
    Function to get user name.

    Returns:
        name

    '''
    clear_console()
    name = input("What is your name? ")
    print(f"Hello {name}! Let's play Battleship.\n")
    return name


def print_board(board, hide_ships=True):
    '''
    Function to print out the board with parameter to hide opponents ship.

    Returns:
        None

    '''
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
    '''
    Randomly places ships on the game board.

    Returns:
        None

    '''
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
    '''
    Function to check if the user's guess is a hit or miss.

    Returns:
        bool: True if the guess is a hit, False if it's a miss.

    '''
    row, col = guess
    if board[row][col] == "O":
        board[row][col] = "X"
        return True
    else:
        board[row][col] = "M"
        return False


def grid_size():
    '''
    Prompts the user to choose the size of the game board.

    Returns:
        int: The size of the game board chosen by the user.

    '''
    clear_console()
    while True:
        board_size_user_choice = input("Choose size of grid from 1-9: \n")

        if board_size_user_choice.isdigit():
            board_size_user_choice = int(board_size_user_choice)

        if board_size_user_choice > 1 <= int(board_size_user_choice) <= 9:
            return board_size_user_choice
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def set_up_player_board(grid_size):
    '''
    Set ups the player board as a list based on the value returned
     from grid_size()

    Returns:
        list of list of str: The player board, represented as a 2D list.

    '''
    clear_console()
    board_size = grid_size
    player_board = []
    for _ in range(board_size):
        player_board.append(["."] * board_size)
    place_ships(player_board, board_size)
    return player_board


def set_up_computer_board(grid_size):
    '''
    Set ups the computer board as a list based on the value returned
    from grid_size()

    Returns:
        list of list of str: The computer board, represented as a 2D list.

    '''
    board_size = grid_size
    computer_board = []
    for _ in range(board_size):
        computer_board.append(["."] * board_size)
    place_ships(computer_board, board_size)
    return computer_board


def update_ship_count(board):
    '''
    Counts the number of ships remaining on the specified game board.

    Returns:
        int: The number of ships remaining on the board.

    '''
    ship_count = 0
    for row in board:
        for cell in row:
            if cell == "O":
                ship_count += 1
    return ship_count


def game_loop(grid_size, name):
    '''
    Game loop function that takes two parameters to run player and
    computer turns, sets the ships counts for the player and computer and sets
    up the boards by calling the functions

    Returns:
        None

    '''
    board_size = grid_size
    computer_ships = board_size - 1
    player_ships = board_size - 1
    player_board = set_up_player_board(board_size)
    computer_board = set_up_computer_board(board_size)

    while computer_ships > 0 or player_ships > 0:
        # Print the board after each round

        print("\nThis is your board:")
        print_board(player_board, False)
        print("\nThis is computer's board:")
        print_board(computer_board, True)

        # Update ship counts

        computer_ships = update_ship_count(computer_board)
        player_ships = update_ship_count(player_board)
        ships = [player_ships, computer_ships]

        if player_turn(board_size, computer_board, name, ships):
            break

        if computer_turn(board_size, player_board, ships):
            break


def player_turn(board_size, computer_board, name, ships):
    '''

    Player turn function that ask user for row and column
    validate the input and check if the player hit the target or/and
    win the game and modifies the 'ships' list.

    Returns:
        None

    '''
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
        if ships[1] > 0:
            ships[1] -= 1
            clear_console()
            print("Congratulations! You sunk a battleship!")
        if ships[1] == 0:
            print(f"\nCongratulations, {name}! You won!")
            return True
    else:
        clear_console()
        print("You missed.")


def computer_turn(board_size, player_board, ships):
    '''
    Function to run computer turn using random lib to generate an integer,
    check if the guess is miss or hit.

    Returns:
        None

    '''
    ships = list(ships)
    print("\nComputer's turn.")
    while True:
        comp_guess_row = random.randint(0, board_size - 1)
        comp_guess_col = random.randint(0, board_size - 1)
        comp_guess = (comp_guess_row, comp_guess_col)
        if (player_board[comp_guess_row][comp_guess_col] != "M" and
                player_board[comp_guess_row][comp_guess_col] != "X"):
            break
    if check_guess(comp_guess, player_board):
        if ships[0] > 0:
            ships[0] -= 1
            print("Oh no! The computer sunk one of your battleships!")
        if ships[0] == 0:
            print("Computer hit your last ship! You lose!")
            return True
    else:
        print("The computer missed.")


def clear_console():
    '''
    Clearing the console.

    Returns:
        None

    '''
    os.system('clear')


def main():
    '''

    Runs the battleship game by calling the necessary functions.
    Prompts the user to enter their name and grid size, and then sets up
    the player and computer boards by calling the appropriate functions.
    Runs the game loop and takes turns between the player and computer
    until one of them has no more ships left. Finally, prints out the
    final board configuration for both the player and computer.

    '''
    try:
        name = get_user_name()
        board_size = grid_size()
        set_up_player_board(board_size)
        set_up_computer_board(board_size)
        game_loop(board_size, name)
    except Exception as err:
        print(str(err))


if __name__ == "__main__":
    main()
