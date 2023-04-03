f = open('words.txt', 'r')
words = f.read().split()

most_double_letters_word = ''
most_double_letters_count = 0

for word in words:

        double_letters_count = 0
        for i in range(len(word)-3):
            if word[i] == word[i+1] and word [i+2] == word[i+3]:
                double_letters_count += 1
                
        if double_letters_count >= most_double_letters_count:
            most_double_letters_count = double_letters_count
            most_double_letters_word = word
            #most_double_letters_word.append(word)
        
        
f.close()

print("The word with the most pairs of consecutive double letters is:", most_double_letters_word)
