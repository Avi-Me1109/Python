c = float(input("Enter your temperature in celsius: "))
# creating an input variable in float to obtain decimal place value of temperature in celsius

f = c * (9/5) + 32
# Using formula to calculate temperature in fahrenheit

print("The temperature in fahrenheit: ", format(f, '.2f'))
# outputting value in fahrenheit in two decimal place