import random
Rows = 3 
Columns = 3 
Board = [] 
AI = ["X", "O"]
Player = ["O", "X"]
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
        user_row = int(input(f"Pick a row: "))
        user_column = int(input(f"Pick a column: "))
        if not (0 <= user_row < Rows and 0 <= user_column < Columns):
            print("Row and column must be between 0 and 2.")
            continue
        if Board[user_row][user_column] != "#":
            print("That location is already taken.")
            continue
        return user_column,user_row
def modify_board():
    user_row, user_column = get_valid_int()
    Board[user_row][user_column] = Player[0]
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
    return all("#" not in row for row in Board)
def play_again():
    while True:
        play_again_q = input("Would you like to play again (Y/N): ").strip().capitalize()
        if play_again_q == "Y":
            return True
        elif play_again_q == "N":
            return False
        print("Please enter Y or N.")
def ai_check_for_winning_move_and_block_player():
    for r in range(Rows):
        if Board[r][0] != "#" and Board[r][0] == Board[r][1] and Board[r][1] == AI[0]:
            if Board[r][2] == "#":
                Board[r][2] = AI[0]
                return False
        if Board[r][1] != "#" and Board[r][1] == Board[r][2] and Board[r][2] == AI[0]:
           if Board[r][0] == "#":
                 Board[r][0] = AI[0]
                 return False
        if Board[r][0] != "#" and Board[r][0] == Board[r][2] and Board[r][2] == AI[0]:
            if Board[r][1] == "#":
                Board[r][1] = AI[0]
                return False
    for c in range(Columns):
         if Board[0][c] != "#" and Board[0][c] == Board[1][c] and Board[1][c] == AI[0]:
             if Board[2][c] == "#":
                 Board[2][c] = AI[0]
                 return False
         if Board[0][c] != "#" and Board[0][c] == Board[2][c] and Board[2][c] == AI[0]:
             if Board[1][c] == "#":
                 Board[1][c] = AI[0]
                 return False
         if Board[1][c] != "#" and Board[1][c] == Board[2][c] and Board[2][c] == AI[0]:
            if Board[0][c] == "#":
                 Board[0][c] = AI[0]
                 return False
    if Board[0][0] != "#" and  Board[0][0] == Board[1][1] and Board[1][1] == AI[0]:
        if Board[2][2] == "#":
           Board[2][2] = AI[0]
           return False
    if Board[1][1] != "#" and Board[1][1] == Board[2][2] and Board[1][1] == AI[0]:
        if Board[0][0] == "#":
           Board[0][0] = AI[0]
           return False
    if Board[0][0] != "#" and Board[0][0] == Board[2][2] and Board[2][2] == AI[0]:
        if Board[1][1] == "#":
            Board[1][1] = AI[0]
            return False
    if Board[1][1] != "#" and Board[0][2] == Board[1][1] and Board[1][1] == AI[0]:
        if Board[2][0] == "#":
            Board[2][0] = AI[0]
            return False
    if Board[1][1] != "#" and  Board[1][1] == Board[2][0] and Board[1][1] == AI[0]:
        if Board[0][2] == "#":
            Board[0][2] = AI[0]
            return False
    if Board[2][0] != "#" and Board[2][0] == Board[0][2] and Board[2][0] == AI[0]:
        if Board[1][1] == "#":
            Board[1][1] = AI[0]
            return False
    # No time to check for blocking
    for r in range(Rows):
        if Board[r][0] != "#" and Board[r][0] == Board[r][1] and Board[r][1] == Player[0]:
            if Board[r][2] == "#":
                Board[r][2] = AI[0]
                return False
        if Board[r][1] != "#" and Board[r][1] == Board[r][2] and Board[r][2] == Player[0]:
           if Board[r][0] == "#":
                 Board[r][0] = AI[0]
                 return False
        if Board[r][0] != "#" and Board[r][0] == Board[r][2] and Board[r][2] == Player[0]:
            if Board[r][1] == "#":
                Board[r][1] = AI[0]
                return False
    for c in range(Columns):
         if Board[0][c] != "#" and Board[0][c] == Board[1][c] and Board[1][c] == Player[0]:
             if Board[2][c] == "#":
                 Board[2][c] = AI[0]
                 return False
         if Board[0][c] != "#" and Board[0][c] == Board[2][c] and Board[2][c] == Player[0]:
             if Board[1][c] == "#":
                 Board[1][c] = AI[0]
                 return False
         if Board[1][c] != "#" and Board[1][c] == Board[2][c] and Board[2][c] == Player[0]:
            if Board[0][c] == "#":
                 Board[0][c] = AI[0]
                 return False
    if Board[0][0] != "#" and  Board[0][0] == Board[1][1] and Board[1][1] == Player[0]:
        if Board[2][2] == "#":
           Board[2][2] = AI[0]
           return False
    if Board[1][1] != "#" and Board[1][1] == Board[2][2] and Board[1][1] == Player[0]:
        if Board[0][0] == "#":
           Board[0][0] = AI[0]
           return False
    if Board[0][0] != "#" and Board[0][0] == Board[2][2] and Board[2][2] == Player[0]:
        if Board[1][1] == "#":
            Board[1][1] = AI[0]
            return False
    if Board[1][1] != "#" and Board[0][2] == Board[1][1] and Board[1][1] == Player[0]:
        if Board[2][0] == "#":
            Board[2][0] = AI[0]
            return False
    if Board[1][1] != "#" and  Board[1][1] == Board[2][0] and Board[1][1] == Player[0]:
        if Board[0][2] == "#":
            Board[0][2] = AI[0]
            return False
    if Board[2][0] != "#" and Board[2][0] == Board[0][2] and Board[2][0] == Player[0]:
        if Board[1][1] == "#":
            Board[1][1] = AI[0]
            return False
    return True 
def take_middle_if_open():
    if Board[1][1] == "#":
        Board[1][1] = AI[0]
        return False
    else:
        return True
def check_for_forks():
  for r in range(Rows):
        # Player on left and middle, empty right
        if Board[r][0] == Player[0] and Board[r][1] == Player[0] and Board[r][2] == "#":
            # Check if the Player[0] can also win somewhere vertically
            for c in range(Columns):
                if Board[0][c] == Player[0] and Board[1][c] == Player[0] and Board[2][c] == "#":
                    Board[r][2] = AI[0]
                    return False
            # Check diagonals
            if r == 0:
                if Board[1][1] == Player[0] and Board[2][2] == "#":
                    Board[r][2] = AI[0]
                    return False
            if r == 2:
                if Board[1][1] == Player[0] and Board[0][2] == "#":
                    Board[r][2] = AI[0]
                    return False
        # Player on middle and right, empty left
        if Board[r][1] == Player[0] and Board[r][2] == Player[0] and Board[r][0] == "#":
            for c in range(Columns):
                if Board[0][c] == Player[0] and Board[1][c] == Player[0] and Board[2][c] == "#":
                    Board[r][0] = AI[0]
                    return False
            if r == 0:
                if Board[1][1] == Player[0] and Board[2][0] == "#":
                    Board[r][0] = AI[0]
                    return False
            if r == 2:
                if Board[1][1] == Player[0] and Board[0][0] == "#":
                    Board[r][0] = AI[0]
                    return False
        # Player on left and right, empty middle
        if Board[r][0] == Player[0] and Board[r][2] == Player[0] and Board[r][1] == "#":
            Board[r][1] = AI[0]
            return False
    # Check columns for forks
  for c in range(Columns):
        # Player top + middle, empty bottom
        if Board[0][c] == Player[0] and Board[1][c] == Player[0] and Board[2][c] == "#":
            if c == 0:
                if Board[0][1] == Player[0] and Board[1][1] == "#":
                    Board[2][c] = AI[0]
                    return False
            if c == 2:
                if Board[0][1] == Player[0] and Board[1][1] == "#":
                    Board[2][c] = AI[0]
                    return False
        # Player middle + bottom, empty top
        if Board[1][c] == Player[0] and Board[2][c] == Player[0] and Board[0][c] == "#":
            if c == 0:
                if Board[2][1] == Player[0] and Board[1][1] == "#":
                    Board[0][c] = AI[0]
                    return False
            if c == 2:
                if Board[2][1] == Player[0] and Board[1][1] == "#":
                    Board[0][c] = AI[0]
                    return False
        # Player top + bottom, empty middle
        if Board[0][c] == Player[0] and Board[2][c] == Player[0] and Board[1][c] == "#":

            Board[1][c] = AI[0]
            return False
    # Check the main diagonal
  if Board[0][0] == Player[0] and Board[1][1] == Player[0] and Board[2][2] == "#":
        Board[2][2] = AI[0]
        return False
  if Board[1][1] == Player[0] and Board[2][2] == Player[0] and Board[0][0] == "#":
        Board[0][0] = AI[0]
        return False
    # Check the other diagonal
  if Board[0][2] == Player[0] and Board[1][1] == Player[0] and Board[2][0] == "#":
        Board[2][0] = AI[0]
        return False
  if Board[1][1] == Player[0] and Board[2][0] == Player[0] and Board[0][2] == "#":
        Board[0][2] = AI[0]
        return False
  return True 
def random_move():
    open_spots=[]
    for r in range(Rows):
        for c in range(Columns):
            if Board[r][c] == "#":
                open_spots.append(r,c)

    if open_spots:
        r,c = random.choice(open_spots)
        Board[r][c] = AI[0]
        return False
    return True

while True: