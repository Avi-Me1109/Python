# Ask the user to enter their name
user = input("Enter your Name (First, Middle, Last) or (First, Last): ")

# Split the user input into a list of names
user = user.split()

# Check if the length of the list is 3, indicating a name in the format "First Middle Last"
if(len(user) == 3):
    # Print the last name followed by a comma
    print(user[2], end = "")
    print(", ", end = "")
    # Print the first name
    print(user[0], end = "")
    print(" ", end = "")
    # Get the first initial of the middle name
    initial = user[1]
    # Print the first initial of the middle name followed by a period
    print(initial[0], end = "")
    print(".")
    
# Check if the length of the list is 2, indicating a name in the format "First Last"
if(len(user) == 2):
    # Print the last name followed by a comma
    print(user[1], end = "")
    print(", ", end = "")
    # Print the first name
    print(user[0], end = "")
    print(" ", end = "")

# Check if the length of the list is less than 2 or greater than 3, indicating an invalid number of names
if(len(user) < 2 or len(user) > 3):
    # Print an error message
    print("Number of names invalid!")
