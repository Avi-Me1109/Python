males = int(input("Enter number of males: "))
females = int(input("Enter number of females: "))

total = males + females

malepercentage = (males/total) * 100
femalepercentage = (females/total) * 100

print("Male Percenntage: ", format(malepercentage, '.2f'), "%")
print("Female Percentage: ", format(femalepercentage, '.2f'), "%")

if(males > females):
    print("More males than females")

else:
    print("More females than males")