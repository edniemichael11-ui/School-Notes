import random

rows = 5
columns = 6
board = []
for row in range(rows):
    board.append([])
    for col in range(columns):
        board[-1].append("X")

def print_board():
    print("  ", end = "")
    for i in range(len(board[0])):
        print(i, end = " ")
    print()
    for i in range(len(board)):
        print(i, end = " ")
        for r in board[i]:
            print(r, end = " ")
        print()


treausre_row = random.randint(0,rows)
treasure_col = random.randint(0, columns)
found = False

while not found:
    print_board()
    userrows = (input("Enter the row you wish to check: "))
    usercolums = int(input("Enter the colums you wish to check: "))
    #we will assume we get ints and they are in range
    if userrows == treausre_row and usercolums == treasure_col:
        print("hooray, you found it")
        board[userrows][usercolums] = "!"
        found = True
    else:
        #If we guess wrong - provide a number saying how far away we are
        row_distance = abs(userrows - treausre_row)
        col_distance = abs(usercolums - treasure_col)
        total_distance = row_distance + col_distance
        board[userrows][usercolums] = total_distance




































#Notes


#for row in range(rows):
#    board.append([])
#    for col in range(columns):
#        board[-1].append("X")
#
#print(board)

# print the board so it looks like:
# X X X X X X
# X X X X X X
# X X X X X X
# X X X X X X
# X X X X X X

#for row in board:
#    for cell in row:
#        print(cell, end=" ")
#
#    print()

# print the board so it looks like:
# make it dynamic so if I change my row and col variables, this still works.
# I'd expect 3 loops - not necessarily all nested
#   0 1 2 3 4 5
# 0 X X X X X X
# 1 X X X X X X
# 2 X X X X X X
# 3 X X X X X X
# 4 X X X X X X

