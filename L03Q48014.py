import random # import the random module

def check(value): # defined a function called check that takes one argument (value)
    number = random.randint(1, 1000) # generate a random integer between 1 and 1000 (inclusive) and store it in number variable
    check = False # initialize check variable to False

    while(check == False): # while check is equal to False
        if(value > number): # if value is greater than number
            value = int(input("Too high. Try again: ")) # prompt user for another guess and convert it to an int type
        
        if(value < number): # if value is less than number
            value = int(input("Too low. Try again: ")) # prompt user for another guess and convert it to an int type
        
        if(value == number): # if value is equal to number
            print("Excellent! You guessed the number!") # print out success message
            check = True # set check to True

a = "Y" #intialize a as yes or 'Y' to run the while loop at least once

while(a == "Y"): 
    print("I have a number between 1 and 1000") 
    print("Can you guess the number?") 
    a = int(input("Please type your first guess: ")) #inputs guess from user and some instructions
    check(a) #running check for the game to procees
    a = input("Would you like to play again (Y or N): ") # check to see if user wants to play again