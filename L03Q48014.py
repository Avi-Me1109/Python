import random

def check(value):
    number = random.randint(1, 1001)
    check = False

    while(check == False):
        if(value > number):
            value = int(input("Too high. Try again: "))
        
        if(value < number):
            value = int(input("Too low. Try again: "))
        
        if(value == number):
            print("Excellent! You guessed the number!")
            check = True

a = "Y"

while(a == "Y"):
    print("I have a number between 1 and 1000")
    print("Can you guess the number?")
    a = int(input("Please type your first guess: "))
    check(a)
    a = input("Would you like to play again (Y or N): ")