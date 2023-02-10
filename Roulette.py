pocketnumber = int(input("Enter your pocket number: "))

color = "none"

if(pocketnumber <= 36 and pocketnumber >= 0):
    check = True

else:
    check = False

if(check == True):
    if(pocketnumber >= 1 and pocketnumber <= 10):
        if(pocketnumber % 2 == 0):
            color = "Black"
        else:
            color = "Red"
    
    elif(pocketnumber >= 11 and pocketnumber <= 18):
        if(pocketnumber % 2 == 0):
            color = "Red"
        else:
            color = "Black"

    elif(pocketnumber >= 19 and pocketnumber <= 28):
        if(pocketnumber % 2 == 0):
            color = "Black"
        else:
            color = "Red"

    elif(pocketnumber >= 29 and pocketnumber <= 36):
        if(pocketnumber % 2 == 0):
            color = "Red"
        else:
            color = "Black"

else:
    print("Error! Invalid Number")

if(check == True):
    print("Your pocket color is: ", color)