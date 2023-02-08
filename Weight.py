mass = float(input("Enter the mass of an object: "))

weight = mass * 9.8

print("The weight of the object: ", weight, "Newtons")

if(weight > 500):
    print("The object is too heavy")

if(weight < 100):
    print("The object is too light")