class Car:

    def __init__(self, model, make):
        self.__year_model = model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed
    
    def get_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make
    
    def set_speed(self, x):
        self.__speed = x
    
    def set_model(self, x):
        self.__year_model = x

    def set_make(self, x):
        self.__make = x

Car1 = Car(2014, "Audi")

print("Accelerating...")
for i in range(5):
    Car1.accelerate()
    print(Car1.get_model(), ",", Car1.get_make(), ":", Car1.get_speed())

print("Braking...")
for i in range(5):
    Car1.brake()
    print(Car1.get_model(), ",", Car1.get_make(), ":", Car1.get_speed())