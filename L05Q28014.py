user = input("Enter your Name (First, Middle, Last): ")

user = user.split()

if(len(user) == 3):
    print(user[2], end = "")
    print(", ", end = "")
    print(user[0], end = "")
    print(" ", end = "")
    initial = user[1]
    print(initial[0], end = "")
    print(".")
    
if(len(user) == 2):
    print(user[1], end = "")
    print(", ", end = "")
    print(user[0], end = "")
    print(" ", end = "")

if(len(user) < 2 or len(user) > 3):
    print("Number of names invalid!")
