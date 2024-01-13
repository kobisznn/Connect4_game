#Author: Kobi Okafor
#Email : kokafor@umass.edu
#Spire ID: 34435539

def make_empty_board(nrows,ncols):
    if 4 <= nrows <= 10 and 4 <=ncols<= 10:
        empty_board = ['.' * ncols for _ in range(nrows)]
    return empty_board
print(make_empty_board(6, 4)) 

def print_board(board):
   boardline="---+"*(len(board[0]) -1)+"---"
   line="   "
   for i in range(len(board)):
       line= board[i]
       for m in range(len(line)):
           if line[m] ==".":
               print('   ',end='')
           elif line[m]=="X":
               print(" X ",end='')
           elif line[m]=="O":
               print (" O ", end='')
           if m==(len(line)-1):
               print("",end='')
           else:
                print('|',end='')
       print("")
       if i !=(len(board)-1):
           print(boardline)

print_board([".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOXX"])


def verify_board(board):
    nrows = len(board)
    ncols = len(board[1])
    no_of_x = 0
    no_of_o = 0
    for i in range(nrows):
        for j in range(ncols):
            cell = board[i][j]
            if cell == "X":
                no_of_x += 1
                if i < nrows - 1 and board[i + 1][j] == ".":
                    return False  
            elif cell == "O":
                no_of_o += 1
                if i < nrows - 1 and board[i + 1][j] == ".":
                    return False  

    return (no_of_x - no_of_o) <= 1
    
def verify_move(board,column_index):
    nrows=len(board)
    ncols=len(board[1])
    if column_index < 0 or column_index >= ncols:
        return False 

    if board[1][column_index] == ".":
        return True  

    return False  
board = ["..O....", "..X....", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
print(verify_move(board, 2)) 

def update_board(board,column_index,player_disc):
    for i in range(len(board)-1,-1,-1):
        for m in range(len(board[i])):
            if m==column_index:
                if board[i][m]==".":
                    update_list=list(board[i])
                    update_list[m]=player_disc
                    board[i]="".join(update_list)
                    return board

board = [".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
print(update_board(board, 0, 'X'))
