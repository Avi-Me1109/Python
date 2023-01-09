#int
num1 = 5
print(num1)

#float
num2 = 6.01
print(num2)

#complex
num3 = 1+2j
print(num3)

#list, modifiable ordered list
cars = ["Audi", "BMW", "Mercedes"]
print(cars[0])
print(cars[1])
print(cars[2])

#tuple, non-modifiable ordered list
product = ('Microsoft', 'XBOX', 499.99)
print(product[0])
print(product[1])
print(product[2])

#String
name = 'Avi'
print (name)

#Set, unordered collection of items
ID = {1, 2, 3, 4}
print(ID)

#Dictionary, elements in pairs, unordered collection
Models = {'R8': 'Audi', 'M8': 'BMW', 'A45': 'Mercedes'}
print(Models)
#OR
print(Models['R8'])

#VARIABLE CONVERSIONS
num1 = '12'
print("num1 is string now", num1)

num1 = int(num1)
print("num1 is now a integer and can be modified", num1+1)