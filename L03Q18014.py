def reverse(x):
    lst = [] # create an empty list to store the digits of the number
    
    a = str(x) # convert the input number to a string
    
    for letter in a: # iterate over each character in the string representation of the input number
        lst.append(letter) # append each character to the list

    lst.reverse() # reverse the order of the list
    
    String = "" # create an empty string

    for number in lst: # iterate over each element in the reversed list
        String += number # concatenate each element to the string
        
    print(String) # print out the final reversed string
    

number = int((input("Enter an integer: "))) # prompt user for an integer input and convert it to an int type
reverse(number) # call reverse function with user's input as argument