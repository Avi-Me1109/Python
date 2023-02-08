# Speed = 70

# print(Speed*6, "miles")
# print(Speed*10, "miles")
# print(Speed*15, "miles")

#code 2

miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the number of gallons used: "))

mpg = miles / gallons

print("Your vehicle averaged ", format(mpg, '.2f'), "miles per gallon")
