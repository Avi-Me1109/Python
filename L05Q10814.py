import string

def space(word):
    space_count = 0
    
    for i in word:
        if(i == " "):
            space_count = space_count+1
    
    return space_count



user = input("Enter your sentence: ")
spaces = space(user)
words = spaces+1
user = user.replace(" ", "")
user = user.upper()
all_freq = {}
 
for i in user:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
print("The number of words in this sentence is: ", words)

for key in all_freq:
    print(key, ' : ', all_freq[key])


