'''
Homework 3, Excercise 4
Osvaldo Canales
February 23, 2023
Develop a tic-tac-toe game 

'''
#Dictionary that acts as a tic-tac-toe cover
board = {
    "top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " "
}

#Will print the board onto the screen 
def printBoard(board):
    print(board["top-L"] + '|' + board["top-M"] + '|' + board["top-R"])
    print('-+-+-')
    print(board["mid-L"] + '|' + board["mid-M"] + '|' + board["mid-R"])
    print('-+-+-')
    print(board["low-L"] + '|' + board["low-M"] + '|' + board["low-R"])

printBoard(board)

player = "X"

#While loop until a player wins, ties, or loses
while True:
    printBoard(board)
    #Have the first person make the move
    move = input(f"Player {player}, enter your move: ")
    #Check for valid input
    if move not in board:
        print("Invalid move. Try again.")
        continue
    #If a player already made a move there
    if board[move] != " ":
        print("That slot is already taken. Try again.")
        continue
    #Switch to other player
    board[move] = player
    #Check to see if the player won the game
    #Long if statement to see if they won, but can be modified in the future
    if (board["top-L"] == board["top-M"] == board["top-R"] == player or
        board["mid-L"] == board["mid-M"] == board["mid-R"] == player or
        board["low-L"] == board["low-M"] == board["low-R"] == player or
        board["top-L"] == board["mid-L"] == board["low-L"] == player or
        board["top-M"] == board["mid-M"] == board["low-M"] == player or
        board["top-R"] == board["mid-R"] == board["low-R"] == player or
        board["top-L"] == board["mid-M"] == board["low-R"] == player or
        board["top-R"] == board["mid-M"] == board["low-L"] == player):
        printBoard(board)
        print(f"Player {player} wins!")
        break
    #If spaces have run out, then declare it as a tie!
    if " " not in board.values():
        printBoard(board)
        print("It's a tie!")
        
    #Player position
    player = "O" if player == "X" else "X"