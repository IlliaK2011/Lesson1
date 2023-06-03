from dog import Dog
class Car:
    def __init__(self, brand):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()

        '''
    def AddPassenger(self, dog = Dog()):
        if(dog.Role == 0):
            self.Passengers.append(dog.Name)
    def AddDriver(self, dog = Dog()):
        if(dog.Role == 1):
            self.Drivers.append(dog.Name)
        '''
    def ToStringPassenger(self, dog = Dog()):
        print(f"Passenger of {self.Brand} is {dog.__str__()}")
    def ToStringDriver(self, dog = Dog()):
        print(f"Driver of {self.Brand} is {dog.__str__()}")
    def AddHumanToCar(self, dog = Dog()):
        if (dog.Role == 0):
            self.Passengers.append(dog.Name)
        if (dog.Role == 1):
            self.Drivers.append(dog.Name)