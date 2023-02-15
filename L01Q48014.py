year = int(input("Enter year (Between 1982 - 2048): "))
check = False
date = 0

if(year >= 1982 and year <= 2048):
    check = True

if(check == True):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19*a) + 24) % 30
    e = ((2*b) + (4*c) + (6*d) + 5) % 7

    date = 22 + d + e

    if(date > 31):
        date = date - 31
        print("The date of easter for the year", year, "is April", date)
    
    else:
        print("The date of easter for the year", year, "is March", date)

else:
    print("Invalid Date (Between 1982 - 2048)!")
