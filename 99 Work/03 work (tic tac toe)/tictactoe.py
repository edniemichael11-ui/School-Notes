Rows = 3 
Columns = 3 
Board = [] 
player = ["X", "O"]
for row in range(Rows): 
    Board.append([]) 
    for col in range(Columns): 
        Board[-1].append("#")
def create_board():
    """Prints the Tic Tac Toe Board"""
    print("  ", end = "")
    for i in range(len(Board[0])):
        print(i, end = " ")
    print()
    for i in range(len(Board)):
        print(i, end = " ")
        for r in Board[i]:
            print(r, end = " ")
        print()
def get_valid_int():
    """Gets an empty board location and returns its row and column."""
    while True:
        user_row = int(input(f"Pick a row ({player[0]}): "))
        user_column = int(input(f"Pick a column ({player[0]}): "))
        if user_row!= user_row.is_integer() or user_column != user_column.is_integer():
            print("Please enter whole numbers.")
        
        if not (0 <= user_row < Rows and 0 <= user_column < Columns):
            print("Row and column must be between 0 and 2.")
            continue
        if Board[user_row][user_column] != "#":
            print("That location is already taken.")
            continue

        return user_row, user_column
def modify_board():
    user_row, user_column = get_valid_int()
    Board[user_row][user_column] = player[0]
def check_for_win():
    for r in range(Rows):
        if Board[r][0] != "#" and Board[r][0] == Board[r][1] == Board[r][2]:
            return True
    for c in range(Columns):
        if Board[0][c] != "#" and Board[0][c] == Board[1][c] == Board[2][c]:
            return True
    if Board[0][0] != "#" and Board[0][0] == Board[1][1] == Board[2][2]:
        return True
    if Board[0][2] != "#" and Board[0][2] == Board[1][1] == Board[2][0]:
        return True
    return False
    
def check_for_tie():
    #be able to explain this - what is all?
    return all("#" not in row for row in Board)
    #Checks every row for "#" if it has none it willr eturn true for each row that has none 
    #but it will return false if it does and the all statements make it to were when only one false is displayed it will become false
def play_again():
    while True:
        play_again_q = input("Would you like to play again (Y/N): ").strip().capitalize()
        if play_again_q == "Y":
            return True
        elif play_again_q == "N":
            return False
        print("Please enter Y or N.")

while True:
    create_board()
    modify_board()
    if check_for_win():
        create_board()
        print(f"Player {player[0]} wins!")
    elif check_for_tie():
        create_board()
        print("Game has ended in a tie.")
    else:
        player.reverse()
        continue

    if not play_again():
        break

    #Be able to explain this (hint: list comprehension)
    Board = [["#" for col in range(Columns)] for row in range(Rows)]
    # generates X columns filled with "#" and then repeats that for x ammount of rows
    player = ["X", "O"]
