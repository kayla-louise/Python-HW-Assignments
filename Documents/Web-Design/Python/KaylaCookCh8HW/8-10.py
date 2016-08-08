#Kayla Cook
#8-10 Tic Tac Toe

#get player 1 name
player1 = input("Player 1, what is your name?")
#get player 2 name
player2 = input("Player 2, what is your name?")
print(player1, " you will be x")
print(player2, " you will be o")
#initalize board
board = [ ['*', '*', '*'],
          ['*', '*', '*'],
          ['*', '*', '*']]
#num turns
turns = 0
# print board
def print_board():
    print("Here is the board, please reference this to select location")
    #print("Column # ", " 0 ", " 1 ", " 2 ")
    #print("Row #  0")
    print((board[0][0]) + (board[0][1]) +(board[0][2]))
    #print("Row #  1 ")
    print((board[1][0]) + (board[1][1]) + (board[1][2]))
    #print("Row #  2 ")
    print((board[2][0]) +(board[2][1]) + (board[2][2]))


#player 1 move
def player1_move (turns):
    if turns < 9:
        print_board()
        print(player1, "please choose location")
        location_x = 0
        location_y = 0
        location_x = (int(input("Please enter the row# (1-3)")) - 1)
        location_y = (int(input("Please enter the column# (1-3)")) - 1)
        while board[location_x][location_y] != '*':
            print("Sorry that location has been taken, choose another")
            location_x = (int(input("Please enter the row# (1-3)")) - 1)
            location_y = (int(input("Please enter the column# (1-3)")) - 1)
        board[location_x][location_y] = 'X'
        turns = turns + 1
        player2_move(turns)
    

#player 2 move
def player2_move (turns) :
    if turns < 9:
        print_board()
        print(player2, "please choose location")
        location_x = 0
        location_y = 0
        location_x = (int(input("Please enter the row# (1-3)")) - 1)
        location_y = (int(input("Please enter the column# (1-3)")) - 1)
        while board[location_x][location_y] != '*':
            print("Sorry that location has been taken, choose another")
            location_x = (int(input("Please enter the row# (1-3)")) - 1)
            location_y = (int(input("Please enter the column# (1-3)")) - 1)
        board[location_x][location_y] = 'O'
        turns = turns + 1
        player1_move(turns)
player1_move(turns)       
#determine winner
#check rows for wins
win = "no"
if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
#check columns for wins
if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
#check for diagonal wins
if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') :
    win = "yes"
    print(player1, " you're the winner!")
if (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O') :
    win = "yes"
    print(player2, " you're the winner!")
if (win == "no"):
    print("It's a tie!")





