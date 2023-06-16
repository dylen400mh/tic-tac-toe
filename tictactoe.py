# print title
def print_title():
    print("Tic-Tac-Toe")
    print("=" * 11 + "\n")

# prints board to display


def print_board(board):
    print("   |   |   ")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   |   |   ")

# clears screen by printing multiple lines


def clear():
    print("\n" * 50)

# function to get position of player's move


def get_player_move():
    move = 0
    in_range = False

    while not in_range or not move.isdigit():
        move = input(
            f"{players[current_player]}, choose a box by entering a number 1-9: ")
        clear()

        if move.isdigit():
            if int(move) not in range(1, 10):  # if not in range 1-9
                print("Out of range! Please enter a valid number.")
            else:
                in_range = True

        if not move.isdigit():
            print("That is not a number. Please enter a valid number.")

    # returns a list containing the row and column
    return get_coordinates(int(move))

# gets location on board according to number selected


def get_coordinates(move):
    row = (move - 1) // 3
    column = (move - 1) % 3
    return row, column

# adds the player's move to the board


def place_move(row, col, current_player):
    board[row][col] = current_player

# switches player turns


def switch_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# runs tic-tac-toe match


def play_match():

    game_in_progress = True

    global board
    board = [[" ", " ", " "], [" ", " ", " "],
             [" ", " ", " "]]  # board starts empty

    global current_player
    current_player = "X"  # player one starts first

    while game_in_progress:

        global winner  # winner variable can be accessed outside the while loop

        print_title()

        # loop will run until player chooses an empty spot
        while True:
            print_board(board)
            row, col = get_player_move()

            if board[row][col] != " ":
                print("This spot is taken. Please choose another spot.")
            else:
                place_move(row, col, current_player)
                switch_turn()
                break

        winner = check_for_winner(board)

        # loop will end if there is a winner
        if winner != None:
            game_in_progress = False

        # if all spots are filled and there is no winner, there will be a tie.

        if full_board(board):
            game_in_progress = False

    print_board(board)
    end_game(winner)  # print result of match

# check for full board


def full_board(board):
    for row in board:
        if " " in row:
            return False
    return True


# checks if there is a winner


def check_for_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# function to print result of the game


def end_game(winner):
    if winner != None:
        print(f"Winner: {players[winner]}")  # announces the winning player
    else:
        print("Tie game!")


def game():
    game_playing = True

    while game_playing:
        play_match()

        choice = ""

        # ask user to play again
        while choice.upper() not in ["Y", "N"]:
            choice = input("Do you want to play again? ")

            if choice.upper() not in ["Y", "N"]:
                print("Invalid Input. Please Try again.")

            # clear screen for new match
            elif choice.upper() == "Y":
                clear()

            # end game
            elif choice.upper() == "N":
                game_playing = False
                break


players = {"X": "Player One", "O": "Player Two"}

game()
