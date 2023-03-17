def generatDivision():
    a = (input("Enter Student Grade Average: ")) # prompt user for student grade average input

    result = "" # initialize result variable as an empty string
    check = True # initialize check variable to True

    for i in a: # iterate over each character in the input string
        if(i.isdigit() == False): # if the character is not a digit
            check = False # set check to False
    

    if(check == True): # if check is True 
        a = int(a) # convert input string to an integer
        if(a >= 0 and a <= 100): # if the input number is within the range of 0 to 100
            if(a >= 60 and a <= 100): 
                result = "First" 

            elif(a >= 45 and a <= 59):
                result = "Second"

            elif(a >= 35 and a <= 44):
                result = "Third"

            else:
                result = "Fail"
            #Checking for all conditions required provided by the question

        else:
            result = "Incorrect Number Format" 

    else:
        result = "Incorrect Number Format" 
    
    return result

Result = generatDivision() # call generatDivision function and store its return value in Result variable
print("Result:", Result) # print out the final result
