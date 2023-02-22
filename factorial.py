a = int(input("Enter an integer: "))

if(a > 0):
    while(a != 2):
        a = (a * (a-1))
    
    print("Answer =", a)

else:
    print("Invalid Number!")