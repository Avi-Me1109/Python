# Open the file 'words.txt' in read-only mode
f = open('words.txt', 'r')

# Read the contents of the file and split the words by whitespace
words = f.read().split()

# Initialize variables to keep track of the word with the most consecutive double letters and its count
most_double_letters_word = ''
most_double_letters_count = 0

# Loop through each word in the list of words
for word in words:

    # Initialize a variable to keep track of the count of consecutive double letters in the word
    double_letters_count = 0
    
    # Loop through each character in the word up to the second-to-last character
    # and check if the current character and the next character are the same, 
    # and if the two characters after them are also the same
    for i in range(len(word)-3):
        if word[i] == word[i+1] and word [i+2] == word[i+3]:
            # If two consecutive pairs of letters are the same, increment the count
            double_letters_count += 1
            
    # If the count of consecutive double letters in the current word is greater than or equal
    # to the count of consecutive double letters in the word with the most consecutive double letters,
    # update the variables to reflect the new word and its count
    if double_letters_count >= most_double_letters_count:
        most_double_letters_count = double_letters_count
        most_double_letters_word = word
        
# Close the file
f.close()

# Print the word with the most consecutive double letters
print("The word with the most pairs of consecutive double letters is:", most_double_letters_word)

