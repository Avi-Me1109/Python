def reverse(x):
    lst = []
    check = True
    
    a = str(x)

    for letter in a:
        if(letter.isdigit() == False):
            print("There is an alphabet in the number")
            check = False

    if(check == True):
        for letter in a:
            lst.append(letter)

        lst.reverse()
        
        String = ""

        for number in lst:
            String += number
        
        print(String)


number = int(input("Enter an integer: "))
reverse(number)