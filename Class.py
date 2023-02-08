males = int(input("Enter number of males: "))
females = int(input("Enter number of females: "))

total = males + females

malepercentage = (males/total) * 100
femalepercentage = (females/total) * 100

print("Male Percenntage: ", malepercentage, "%")
print("Female Percentage: ", femalepercentage, "%")