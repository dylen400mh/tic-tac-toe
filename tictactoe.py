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
        print_board(board)
        move = input("Choose a box by entering a number 1-9: ")
        clear()

        if move.isdigit():
            if int(move) not in range(1,10): # if not in range 1-9
                print("Out of range! Please enter a valid number.")
            else:
                in_range = True

        if not move.isdigit():
            print("That is not a number. Please enter a valid number.")

    return get_coordinates(int(move)) # returns a list containing the row and column

# adds the player's move to the board
def place_move(row, col, current_player):
    board[row][col] = current_player

# switches player turns
def switch_turn():
    global current_player
    if current_player == PLAYER_ONE :
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE

# runs tic-tac-toe game
def game():

    is_won = False

    while not is_won:

        # loop will run until player chooses an empty spot
        while True:
            row, col = get_player_move()

            if board[row][col] != " ":
                print("This spot is taken. Please choose another spot.")
            else:
                place_move(row, col, current_player)
                switch_turn()
                break

        winner = check_for_winner(board)

        if winner != None:
            is_won = True

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

# gets location on board according to number selected
def get_coordinates(move):
    row = (move - 1) // 3
    column = (move - 1) % 3
    return row, column


board = [[" "," "," "],[" "," "," "],[" "," "," "]] # board starts empty

PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE # player one starts first

# numbered locations corresponding with the 2D array positions of the board
locations = {1: board[0][0],
             2: board[0][1],
             3: board[0][2],
             4: board[1][0],
             5: board[1][1],
             6: board[1][2],
             7: board[2][0],
             8: board[2][1],
             9: board[2][2]}

game()










