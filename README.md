<h1 align="center">Battleship Game!</h1>

This is a simple implementation of the classic Battleship game in Python. The objective of the game is to sink all of the opponent's ships before they sink yours.

# Instruction 

1. The game starts by prompting the player to enter their name.
2. The player selects the size of the grid they want to play on (between 1 and 9).
3. The player and the computer each place 4 ships on the grid. The location of the ships is randomized.
4. The game then begins, with the player and the computer taking turns guessing the location of the opponent's ships on the grid.
5. If a player successfully guesses the location of one of their opponent's ships, that ship is considered "sunk". The game ends when all of one player's ships have been sunk.


# Features

##  This implementation of Battleship has the following features:

-  The player can select the size of the grid they want to play on.
-  The location of the ships is randomized for both the player and the computer.
-  The player and the computer take turns guessing the location of the opponent's ships on the grid.
-  If a player successfully guesses the location of one of their opponent's ships, that ship is considered "sunk".
-  The game ends when all of one player's ships have been sunk.
-  The game displays the final board after the game has ended.

# Data Model

The game is played on a 2-dimensional grid, with each cell on the grid representing a location on the game board. The game board is represented by a 2-dimensional list in Python, with each cell containing either a "." (empty cell), "O" (a cell containing a ship), "X" (a cell that has been hit), or "M" (a cell that has been missed).

# Testing 

This code has been tested on Python 3.9.5 on Windows 10.

-   Data validation for user inputs. Does not take wrong inputs and loop the game again.
-   User choice of hit can not be out of the grid spec.

# Solved bugs

-   There was a bug in computer_turn function, because I was trying to modify a tuple that I received. I fixed it by converting tuple to a list.

# Validator testing

-   Code has no errors when passing through [CI Python Linter](https://pep8ci.herokuapp.com/)

# Deployment

-   Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to repository
    - Click on Deploy

# Credits

-  Code Institute for the deployment terminal and the sample of the idea to create battleship game