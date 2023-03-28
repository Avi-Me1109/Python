# Defining a function 'win' that takes the current state of the board as input and checks if any player has won
def win(a):
    # Initializing a variable 'b' to store the winning player (if any)
    b = "none"

    # Checking if any player has won by matching three consecutive cells in a row
    if(a[0] != " " and a[1] != " " and a[2] != " "):
        if(a[0] == a[1] and a[0] == a[2]):
            b = a[0]
    
    if(a[3] != " " and a[4] != " " and a[5] != " "):
        if(a[3] == a[4] and a[3] == a[5]):
            b = a[3]
    
    if(a[6] != " " and a[7] != " " and a[8] != " "):
        if(a[6] == a[7] and a[6] == a[8]):
            b = a[6]

    # Checking if any player has won by matching three consecutive cells in a column
    if(a[0] != " " and a[3] != " " and a[6] != " "):
        if(a[0] == a[3] and a[0] == a[6]):
            b = a[0]
    
    if(a[1] != " " and a[4] != " " and a[7] != " "):
        if(a[1] == a[4] and a[1] == a[7]):
            b = a[1]
    
    if(a[2] != " " and a[5] != " " and a[8] != " "):
        if(a[2] == a[5] and a[2] == a[8]):
            b = a[2]

    # Checking if any player has won by matching three consecutive cells in a diagonal
    if(a[0] != " " and a[4] != " " and a[8] != " "):
        if(a[0] == a[4] and a[0] == a[8]):
            b = a[0]
    
    if(a[2] != " " and a[4] != " " and a[6] != " "):
        if(a[2] == a[4] and a[2] == a[6]):
            b = a[2]
        
    # Returning the winning player (if any)
    return b

# Defining a function 'draw' that takes the current state of the board as input and checks if the game has ended in a draw
def draw(a):
    # Initializing a variable 'drawcheck' to False
    drawcheck = False

    # Checking if all cells on the board have been filled with Xs or Os
    for i in range(len(a)):
        if (a[i] == "X" or a[i] == "O"):
            drawcheck = True
        
        else:
            drawcheck = False
            break

    # Returning True if the game has ended in a draw, False otherwise
    return drawcheck
    
# Defining a function 'board' that takes the current state of the board as input and prints it on the screen
def board(a):
    print(a[0], "|", a[1], "|", a[2])
    print("---------")
    print(a[3], "|", a[4], "|", a[5])
    print("---------")
    print(a[6], "|", a[7], "|", a[8])
    print(" ")

#The code initializes an empty list row1 that represents the initial state of the Tic Tac Toe board.
row1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#The variable check is initialized to False, which is used to keep track of the game's status (whether the game has ended or not).
check = False

#The while loop runs until check is True, which means that the game has ended.
while(check == False):
    #In each iteration of the loop, the board function is called to display the current state of the board.
    board(row1)

    #The first player (Player1) is asked to enter their move by inputting a position number between 1 and 9. The position number corresponds to the location on the board where they want to place their marker ("X").
    p1 = int(input("Player1 enter position: "))
    #The value in the row1 list at the selected position is updated to "X".
    row1[p1-1] = "X" 
    board(row1)

    #The win function is called to check if the game has ended with a win by any player. If a winner is found, the check variable is set to True, and the game ends. The winner is displayed on the screen.
    Winner = win(row1)
    if(Winner != "none"):
        check = True
        print("Game Over!\nWinner is ", Winner)
        break

    #The draw function is called to check if the game has ended in a draw. If the board is completely filled with X's and O's, the check variable is set to True, and the game ends with a draw.
    Draw = draw(row1)
    if(Draw == True):
        check = True
        print("Game Over!\nDraw!")
        break
    
    #The second player (Player2) is asked to enter their move by inputting a position number between 1 and 9.
    p2 = int(input("Player2 enter position: "))
    #The value in the row1 list at the selected position is updated to "O".
    row1[p2-1] = "O"
    board(row1)

    #same process as player 1
    Winner = win(row1)
    if(Winner != "none"):
        check = True
        print("Game Over!\nWinner is ", Winner)

    Draw = draw(row1)
    if(Draw == True):
        check = True
        print("Game Over!\nDraw!")
        break
    
    #If neither a win nor a draw is found, the loop continues with the next iteration, and the game continues until there is a winner or a draw.