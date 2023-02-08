amount = float(input("Enter the total amount of your order: "))
tip = amount * 0.18
service = amount * 0.07

print("Intital amount: ", amount)
print("Tip amount(18%): ", format(tip, '.2f'))
print("Service Tax(7%): ", format(service, '.2f'))
print("Final amount: ", (amount + tip + service))