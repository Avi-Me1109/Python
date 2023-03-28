# Importing the 'random' module to generate random numbers
import random

# Defining a function 'roll' that takes the number of throws as input
def roll(throws):
    
    # Creating an empty list to store the dice rolls
    lt = []
    
    # Looping through the number of throws
    for i in range(throws):
        # Appending a random number between 1 and 6 (inclusive) to the list
        lt.append(random.randint(1,6))
        
        # Sorting the list after each throw
        lt.sort()

    # Returning the sorted list of dice rolls
    return lt

# Prompting the user to enter the number of throws
no_of_throws = int(input("Enter the number of throws: "))

# Calling the 'roll' function with the user input as argument and storing the result in a variable
sorted_listed = roll(no_of_throws)

# Printing the sorted list of dice rolls
print(sorted_listed)
