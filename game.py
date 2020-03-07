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
    #Two diagnol win possibilities
    elif(board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_') or (board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_'):
        return True
    else:
        return False

#This function checks if is free and unplayed on so far
def spot_free(xcor, ycor, board):
    if(board[xcor][ycor] != "_"):
        return False
    else:
        return True

#This function checks if the x and y coordinates are out of the boundaries of the board
def out_of_bounds(xcor, ycor):
    if(0 <= xcor <= 2) and (0 <= ycor <=2):
        return False
    else:
        return True

#This function checks if the x and y from the user input were numbers
def input_is_number(xcor, ycor):
    return xcor.isdigit() and ycor.isdigit()



#counter to keep track of turns
count = 0
player = "Player 1"
print_board(ttboard)
while(count < 9):
    print("Your turn", player)
    print()
    x = input("Please input your x coordinate: ")
    y = input("Please input your y coordinate: ")
    print()
    
    correct_input = input_is_number(x,y)
    while(not correct_input):
        x = input("Please input an x coordinate that is a number: ")
        y = input("Please input a y coordinate that is a number: ")
        correct_input = input_is_number(x,y)
        print()
    
    x = int(x)
    y = int(y)
    print()
    bound_status = out_of_bounds(x,y)
    while(bound_status):
        x = int (input("Please input an x coordinate that is in the valid range: "))
        y = int (input("Please input a y coordinate that is in the valid range: "))
        bound_status = out_of_bounds(x,y)
        print()
        
    not_taken = spot_free(x, y, ttboard)
    while(not not_taken):
        x = int (input("Please input a new x coordinate that because that x-y pair has already been played: "))
        y = int (input("Please input a new y coordinate that because that x-y pair has already been played: "))
        not_taken = spot_free(x, y, ttboard)
        print()

    
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

if(not check_for_winner(ttboard)):
    print('The game is a CAT!  =^..^= (")(")')

    









