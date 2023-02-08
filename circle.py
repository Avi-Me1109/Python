import math

radius = float(input("Enter the radius: "))

area = math.pi * (radius * radius)
circumference = math.pi * 2 * radius

print("The circumference is: ", format(area, '.2f'))
print("The area is: ", format(circumference, '.2f'))
