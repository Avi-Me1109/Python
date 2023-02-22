a = 0

for i in range (0,5):
    string = input("Enter a word: ")
    print("The length of the word is", len(string), "letters")
    a = a + len(string)

print("The average length of the word is", a/5)