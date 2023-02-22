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

    elif(comp == 3 and person == 1):
        winner = 2

    elif(comp == 3 and person == 2):
        winner = 1

    elif(comp == 2 and person == 1):
        winner = 2

    elif(comp == 1 and person == 2):
        winner = 1

    elif(comp == 2 and person == 3):
        winner = 2
    
    else:
        winner = 0

cont = True

while(cont == True):
    computer, computervalue = compchoice()

    choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

    person, personvalue = peoplechoice(choice)

    print(computer)

    check = win(computervalue, personvalue)

    if(check == 1):
        print("Computer wins!")

    if(check == 2):
        print("You win!")

    urlife = int(input("Enter 1 if you want to continue or 0 if you want to stop this madness: "))

    if(urlife == 1):
        cont = True

    else:
        cont = False



