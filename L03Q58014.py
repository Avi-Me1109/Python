import random

# Function to generate a random number between 1 and 3 to represent the computer's choice
def computer_choice():
    a = random.randint(1, 3)
    return a

# Function to determine the winner based on the player's choice and the computer's choice
def winner(player_choice, computer):
    # Convert the computer's choice (represented by a number) to a string that represents the corresponding option
    if(computer == 1):
        a = "bird"
    elif(computer == 2):
        a = "stone"
    else:
        a = "water"

    # Determine the winner based on the player's choice and the computer's choice
    if player_choice == a:
        return "Draw"
    elif player_choice == "stone" and computer == 1:
        return "You win! Stone knocks Bird."
    elif player_choice == "bird" and computer == 2:
        return "You lose! Stone knocks Bird."
    elif player_choice == "water" and computer == 1:
        return "You lose! Bird drinks Water."
    elif player_choice == "bird" and computer == 3:
        return "You win! Bird drinks Water."
    elif player_choice == "water" and computer == 2:
        return "You win! Stone sinks/drowns in Water."
    elif player_choice == "stone" and computer == 3:
        return "You lose! Stone sinks/drowns in Water."
    else:
        return "Invalid choice. Choose from bird, stone, or water."

# Function to check if the player and computer choices are the same, resulting in a draw
def draw(player_choice, computer):
    if player_choice == computer:
        return True
    else:
        return False

# Function to convert the computer's choice (represented by a number) to a string that represents the corresponding option
def computer_word(choice):
    a = ""
    if(choice == 1):
        a = "bird"
    elif(choice == 2):
        a = "stone"
    else:
        a = "water"
    return a

# Set a flag to keep track of whether there is a draw or not
draw_check = True

# Loop until there is no draw
while(draw_check == True):
    # Get the computer's choice and the player's choice
    comp_choice = computer_choice()
    player_choice = input("Choose bird, stone, or water: ").lower()
    computer_voice = computer_word(comp_choice)
    
    # Print the computer's choice and determine the winner
    print("Computer chooses:", computer_voice)
    draw_check = draw(player_choice, computer_voice)
    print(winner(player_choice, comp_choice))
