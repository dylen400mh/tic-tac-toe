
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

board = [" "," "," "," "," "," "," "," "," "] # starts empty




