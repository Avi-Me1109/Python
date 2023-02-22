import random

def guessing(answer, guess):
    
    a = False

    if(guess > answer):
        print("Too high, try again.")
    
    if(guess < answer):
        print("Too low, try again.")
    
    if(guess == answer):
        print("Congratulations! You have won nothing. Do you think spending hours was worth it?")
        a = True
    
    return a


a = random.randint(1, 100)
check = False
cont = True

while(cont == True):
    while (check == False):
        answer = int(input("Enter your guess: "))

        check = guessing(a, answer)

    urlife = int(input("Enter 1 if you want to continue or 0 if you want to stop this madness: "))

    if(urlife == 1):
        cont = True

    else:
        cont = False



