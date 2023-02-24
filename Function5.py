import random

def compchoice():
    choice = random.randint(1,3)
    wordchoice = ""

    if(choice == 1):
        wordchoice = "rock"
    
    if(choice == 2):
        wordchoice = "paper"

    if(choice == 3):
        wordchoice = "scissors"

    return wordchoice, choice

def peoplechoice(choice):
    wordchoice = ""

    if(choice == 1):
        wordchoice = "rock"
    
    if(choice == 2):
        wordchoice = "paper"

    if(choice == 3):
        wordchoice = "scissors"

    return wordchoice, choice

def win (comp, person):
    winner = 0

    if(comp == 1 and person == 3):
        winner = 1

    if(comp == 3 and person == 1):
        winner = 2

    if(comp == 3 and person == 2):
        winner = 1

    if(comp == 2 and person == 1):
        winner = 2

    if(comp == 1 and person == 2):
        winner = 1

    if(comp == 2 and person == 3):
        winner = 2

    return winner

cont = True

while(cont == True):
    computer, computervalue = compchoice()

    choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

    person, personvalue = peoplechoice(choice)

    print("Computer has chose", computer)

    check = win(computervalue, personvalue)

    if(check == 1):
        print("Computer wins!")
        urlife = int(input("Try again? (Enter Y or N): "))

        if(urlife == "Y"):
            cont = True

        else:
            cont = False

    if(check == 2):
        print("You win!")
                
        urlife = int(input("Try again? (Enter Y or N): "))

        if(urlife == "Y"):
            cont = True

        else:
            cont = False

    else:
        print("Nobody wins!")




