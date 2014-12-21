from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
for turn in range(4):
    # Be sure to indent four spaces!
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            print "Please try again."
#            turn -= 1                                                                  Why doesn't this work? The "Game Over" message does not get displayed at the end of the game if such a case arises (but the game still ends!), which means the value of turn does not reach 3. But still when 'turn + 1' is printed, the value gets incremented even if such a condition is encountered. 
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            print "Please try again."
#            turn -= 1                                                                  Same as last message.
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)
print "Game Over"