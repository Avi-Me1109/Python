item1 = float(input("Enter the price of your first item: "))
item2 = float(input("Enter the price of your second item: "))
item3 = float(input("Enter the price of your third item: "))
item4 = float(input("Enter the price of your fourth item: "))
item5 = float(input("Enter the price of your fifth item: "))

subtotal = item1 + item2 + item3 + item4 + item5
salesTax = 0.06 * subtotal

print("Subtotal of Items: ", format(subtotal, '.2f'))
print("Sales Tax (6%): ", format(salesTax, '.2f'))
print("Final Total: ", format(subtotal + salesTax, '.2f'))