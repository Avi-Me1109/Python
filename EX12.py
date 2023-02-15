quantity = int(input("Enter the amount of packages purchased: "))
discount = 0.0

if((quantity >= 10) and (quantity <= 19)):
    discount = 0.1

elif((quantity >= 20) and (quantity <= 49)):
    discount = 0.2

elif((quantity >= 50) and (quantity <= 99)):
    discount = 0.3

elif((quantity >= 100)):
    discount = 0.4
    
else:
    discount = 0

price = quantity * 99
discountprice = discount * price
final = price - discountprice

print("Total Packages: ", quantity)
print("Price before Discount: ", quantity * 99)
print("Discount Received: ", round(discount*100), "%")
print("Final Price: ", final)