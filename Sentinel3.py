string = "a"
a = 0
b = 0

while(string != ""):
    string = input("Enter a word: ")
    a = a + len(string)
    b = b+1

print("The average length for", b, "words is", int(a/b), "letters")