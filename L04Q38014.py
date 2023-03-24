import random

def win(a):

    b = "none"

    if(a[0] != " " and a[1] != " " and a[2] != " "):
        if(a[0] == a[1] and a[0] == a[2]):
            b = a[0]
    
    if(a[3] != " " and a[4] != " " and a[5] != " "):
        if(a[3] == a[4] and a[3] == a[5]):
            b = a[3]
    
    if(a[6] != " " and a[7] != " " and a[8] != " "):
        if(a[6] == a[7] and a[6] == a[8]):
            b = a[6]

    if(a[0] != " " and a[3] != " " and a[6] != " "):
        if(a[0] == a[3] and a[0] == a[6]):
            b = a[0]
    
    if(a[1] != " " and a[4] != " " and a[7] != " "):
        if(a[1] == a[4] and a[1] == a[7]):
            b = a[1]
    
    if(a[2] != " " and a[5] != " " and a[8] != " "):
        if(a[2] == a[5] and a[2] == a[8]):
            b = a[2]

    if(a[0] != " " and a[4] != " " and a[8] != " "):
        if(a[0] == a[4] and a[0] == a[8]):
            b = a[0]
    
    if(a[2] != " " and a[4] != " " and a[6] != " "):
        if(a[2] == a[4] and a[2] == a[6]):
            b = a[2]
        
    return b

def draw(a):
    drawcheck = False

    for i in range(len(a)):
        if (a[i] == "X" or a[i] == "O"):
            drawcheck = True
        
        else:
            drawcheck = False
            break
    return drawcheck

def computer():
    value = random.randint(1,9)
    return value
    
def board(a):
    print(a[0], "|", a[1], "|", a[2])
    print("---------")
    print(a[3], "|", a[4], "|", a[5])
    print("---------")
    print(a[6], "|", a[7], "|", a[8])
    print(" ")

row1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
check = False

while(check == False):
    board(row1)
    p1 = int(input("Player1 enter position: "))
    row1[p1-1] = "X" 
    board(row1)

    Winner = win(row1)
    if(Winner != "none"):
        check = True
        print("Game Over!\nWinner is ", Winner)
        break

    Draw = draw(row1)
    if(Draw == True):
        check = True
        print("Game Over!\nDraw!")
        break

    print("Computer entering position...")
    check2 = False
    while(check2 == False):
        p2 = computer()
        if(row1[p2-1] == " "):
            check2 = True

    row1[p2-1] = "O"
    board(row1)

    Winner = win(row1)
    if(Winner != "none"):
        check = True
        print("Game Over!\nWinner is ", Winner)

    Draw = draw(row1)
    if(Draw == True):
        check = True
        print("Game Over!\nDraw!")
        break