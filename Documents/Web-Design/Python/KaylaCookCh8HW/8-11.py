#Kayla Cook
#8-11 Lo Shu Magic Square

#initalize board w/ positions
samp_board = [ [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

#initalize board
board = [ [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

#print board
def print_samp_board():
    print("Here is a sample board")
    print("The numbers correspond to location numbers")
    print((samp_board[0][0]), (samp_board[0][1]), (samp_board[0][2]))
    print((samp_board[1][0]), (samp_board[1][1]), (samp_board[1][2]))
    print((samp_board[2][0]), (samp_board[2][1]), (samp_board[2][2]))

#get users numbers
location = 1
rows = 3
cols = 3
row = 0
while row < rows:
    col = 0
    while col < cols:
        print_samp_board()
        print("We are filling out location # ", location)
        board[row][col] = int(input("please enter a number 1-9:"))
        col += 1
        location += 1
    row += 1
        
                          
#determine if lo shu magic square
                          #horizontal totals
total_1 = ((board[0][0]) + (board[0][1]) + (board[0][2]))
total_2 = ((board[1][0]) + (board[1][1]) + (board[1][2]))
total_3 = ((board[2][0]) + (board[2][1]) + (board[2][2]))
                          #vertical totals
total_4 = ((board[0][0]) + (board[1][0]) + (board[2][0]))                         
total_5 = ((board[0][1]) + (board[1][1]) + (board[2][1]))                 
total_6 = ((board[0][2]) + (board[1][2]) + (board[2][2]))
                          #diagonal totals
total_7 = ((board[0][0]) + (board[1][1]) + (board[2][2]))
total_8 = ((board[0][2]) + (board[1][1]) + (board[2][0]))

if (total_1 == total_2 == total_3 == total_4 == total_5 == total_6
    == total_7 == total_8):
                print("This is a Lo Shu Magic Square!")
else:
                print("This is not a Lo Shu Magic Square")
