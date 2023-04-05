# Importing the string module to use its string-related operations
import string

# Defining a function called space which takes a word as input
def space(word):
    # Initializing a variable to count the number of spaces
    space_count = 0
    
    # Looping through each character in the word
    for i in word:
        # If the character is a space, increment the space count
        if(i == " "):
            space_count = space_count+1
    
    # Return the space count
    return space_count

# Asking the user to input a sentence and storing it in the variable 'user'
user = input("Enter your sentence: ")

# Calling the 'space' function to count the number of spaces in the user input
spaces = space(user)

# Adding 1 to the number of spaces to get the total number of words
words = spaces+1

# Removing spaces, full stops and commas from the user input and converting it to uppercase
user = user.replace(" ", "")
user = user.replace(".", "")
user = user.replace(",", "")
user = user.upper()

# Initializing an empty dictionary to store character frequencies
all_freq = {}

# Looping through each character in the modified user input
for i in user:
    # If the character is already in the dictionary, increment its count
    if i in all_freq:
        all_freq[i] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        all_freq[i] = 1
        
# Printing the number of words in the sentence
print("The number of words in this sentence is: ", words)

# Looping through each key-value pair in the 'all_freq' dictionary
for key in all_freq:
    # Printing the key (character) and its count
    print(key, ' : ', all_freq[key])
