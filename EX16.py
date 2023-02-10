year = int(input("Enter a year: "))

if(year % 100 == 0):
    if(year % 400 == 0):
        print("February has 29 days")

elif(year % 4 == 0):
    print("February has 29 days")

else:
    print("February has 28 days")