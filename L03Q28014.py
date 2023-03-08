def generatDivision():

    a = (input("Enter Student Grade: "))

    result = ""
    check = True

    for i in a:
        if(i.isdigit() == False):
            check = False
    

    if(check == True):
        a = int(a)
        if(a >= 0 and a <= 100):
            if(a >= 60 and a <= 100):
                result = "First"

            elif(a >= 45 and a <= 59):
                result = "Second"

            elif(a >= 35 and a <= 44):
                result = "Third"

            else:
                result = "Fail"

        else:
            result = "Incorrect Number Format"

    else:
        result = "Incorrect Number Format"
    
    return result

Result = generatDivision()
print("Result:", Result)
