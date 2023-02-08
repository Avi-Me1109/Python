principalAmount = float(input("Enter original amount of money deposited in the account: "))
interestRate = float(input("Enter the annual interest rate: ")) / 100
compoundingNumber = int(input("Enter how many times the interest is added: "))
years = int(input("Enter number of years for desired year of checking:" ))

Amount = principalAmount * ((1 + interestRate/compoundingNumber) ** (compoundingNumber * years))


print("The current balance in the bank account is ", format(Amount, '.2f'))