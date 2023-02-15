#Avi Raj Balam
#Lab 1 - Question 4
#13/02/2023
#A program that inputs a year, verifies that it is in the proper range, and then prints out the date of Easter that year.


#Declaration of variables + user input prompt
year = int(input("Enter year (Between 1982 - 2048): "))
check = False
date = 0

#Condition check for user input that will determine boolean value of "check" variable
if(year >= 1982 and year <= 2048):
    check = True

#If boolean value is changed following block will run
if(check == True):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19*a) + 24) % 30
    e = ((2*b) + (4*c) + (6*d) + 5) % 7

    date = 22 + d + e
    
#"date" variables value is dependent on the block above, its value is then used as an argument to determine output message

    if(date > 31):
        date = date - 31
        print("The date of easter for the year", year, "is April", date)
    
    else:
        print("The date of easter for the year", year, "is March", date)

else:
    print("Invalid Date (Between 1982 - 2048)!")