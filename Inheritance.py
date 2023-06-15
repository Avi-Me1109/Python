class Bird:
    def __init__(self, bird_type):
        self.__bird_type = bird_type

    def get_birdType(self):
        return self.__bird_type

class Duck (Bird):
    pass

bird1 = Duck("duck")
print(bird1.get_birdType())
