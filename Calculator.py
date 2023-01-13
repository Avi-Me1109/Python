print("Welcome to Calculator")

Operation = input("Enter your operation symbol: ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = 0

if Operation == '+':
    num3 = num1 + num2
    print("Answer = ", num3)

elif Operation == '-':
    num3 = num1 - num2
    print("Answer = ", num3)

elif Operation == 'x':
    num3 = num1 * num2
    print("Answer = ", num3)

elif Operation == '/':
    num3 = num1 / num2
    print("Answer = ", num3)

else:
    print("No valid Operation")

exit()