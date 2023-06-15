# prints board to display
def print_board(board):
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

# clears screen by printing multiple lines
def clear():
    print("\n" * 50)

# function to get position of player's move
def get_player_move():
    move = 0

    while int(move) not in range(1,10) or not move.isdigit():
        print_board(board)
        move = input("Choose a box by entering a number 1-9: ")
        clear()

        if move.isdigit():
            if int(move) not in range(1,10):
                print("Out of range! Please enter a valid number.")

        if not move.isdigit():
            print("That is not a number. Please enter a valid number.")
    
    return int(move)

# adds the player's move to the board
def place_move(move, current_player):
    board[move - 1] = current_player

# switches player turns
def switch_turn():
    global current_move
    if current_move == PLAYER_ONE :
        current_move = PLAYER_TWO
    else:
        current_move = PLAYER_ONE

# runs tic-tac-toe game
def game():
    while not isWon:
        place_move(get_player_move(), current_player)


board = [" "," "," "," "," "," "," "," "," "] # board starts empty

PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE # player one starts first

isWon = False

game()










