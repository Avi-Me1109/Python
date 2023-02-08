sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48

cookienumber = int(input("Enter the number of cookies you want: "))

print("Cups of Sugar Required: ", format(sugar * cookienumber, '.2f'))
print("Cups of Butter Required: ", format(butter * cookienumber, '.2f'))
print("Cups of Flour Required: ", format(flour * cookienumber, '.2f'))