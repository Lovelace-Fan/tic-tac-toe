# Tic Tac Toe Game

rows, columns = (3, 3)


board = [["_"] * columns for j in range(rows) ]

#Function to print the board out
def print_board(board):
    for row in board:
        print(row)

#counter to keep track of turns
count = 0
player = "Player 1"

while(count < 9):
    print("Your turn", player)
    print()
    print_board(board)
    
    x = int (input("Please input your x coordinate: "))
    y = int (input("Please input your y coordinate: "))
    print()
    if(player == "Player 1"):
        board[x][y] = "X"
        player = "Player 2"
        
    else:
        board[x][y] = "O"
        player = "Player 1"
        
    print()
    









