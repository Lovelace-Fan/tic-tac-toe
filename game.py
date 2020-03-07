# Tic Tac Toe Game

rows, columns = (3, 3)


ttboard = [["_"] * columns for j in range(rows) ]

#Function to print the board out
def print_board(board):
    for row in board:
        print(row)
        
        
        
def check_for_winner(board):
    #Three horizontal win possibilities
    if(board[0][0] == board[0][1] == board[0][2] and board[0][0] != '_') or (board[1][0] == board[1][1] == board[1][2] and board[1][0] != '_') or (board[2][0] == board[2][1] == board[2][2] and board[2][0] != '_'):
        return True
    #Three vertical win possibilties
    elif(board[0][0] == board[1][0] == board[2][0] and board[0][0] != '_') or (board[0][1] == board[1][1] == board[2][1] and board[0][1] != '_') or (board[0][2] == board[1][2] == board[2][2] and board[0][2] != '_'):
        return True
    #Two diagnols
    elif(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_') or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_'):
        return True
    else:
        return False



#counter to keep track of turns
count = 0
player = "Player 1"
print_board(ttboard)
while(count < 9):
    print("Your turn", player)
    print()
    
    
    x = int (input("Please input your x coordinate: "))
    y = int (input("Please input your y coordinate: "))
    print()
    if(player == "Player 1"):
        ttboard[x][y] = "X"
        print_board(ttboard)
        if(check_for_winner(ttboard)):
            print('\n{} is the Winner!'.format(player))
            break
        player = "Player 2"
        
    else:
        ttboard[x][y] = "O"
        print_board(ttboard)
        if(check_for_winner(ttboard)):
            print('\n{} is the Winner!'.format(player))
            break
        player = "Player 1"
        
    print()
    count += 1
    

    









