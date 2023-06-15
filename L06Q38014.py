class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, x):
        self.__name = x

    def get_name(self):
        return self.__name    
    
    def set_animaltype(self, x):
        self.__animal_type = x

    def get_animaltype(self):
        return self.__animal_type
    
    def set_age(self, x):
        self.__age = x

    def get_age(self):
        return self.__age
    
name = input("Enter your pet's name: ")
animal = input("Enter the type of your animal: ")
age = input("Enter the age of your pet: ")
Pet1 = Pet(name, animal, age)

print("Name:", Pet1.get_name())
print("Animal:", Pet1.get_animaltype())
print("Age:", Pet1.get_age())
 