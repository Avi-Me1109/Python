purchase = float(input("Enter the amount of your purchase: "))

installmentno = int(input("Enter number of installments wanted: "))

purchase = purchase + (purchase * 0.05)

installmentprice = purchase / installmentno

print("The total amount of your purchase: ", purchase)
print("The payment per installment: ", installmentprice)