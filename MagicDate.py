month = int(input("Enter a month in numerical form: "))
day = int(input("Enter a day in numerical form: "))
year = int(input("Enter a year in numerical form: "))

check = month * day

if(check == year):
    print("The date is magic!")

else:
    print("The date is not magic")
