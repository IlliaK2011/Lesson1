from car import Car
from dog import Dog

vlad = Dog("Vlad", 1)
mikita = Dog("Mikita", 1)
illia = Dog("Illia", 1)
andrii = Dog("Andrii", 0)
bronislav = Dog("Bronislav", 0)

dog = list()
dog.append(vlad)
dog.append(mikita)
dog.append(illia)
dog.append(andrii)
dog.append(bronislav)
car = Car("BMW x6")
for dog in dogs:
    car.AddHumanToCar(dog)
    #car.AddPassenger(dog)
    #car.AddDriver(dog)

for passenger in car.Passengers:
    car.ToStringPassenger(passenger)
for driver in car.Drivers:
    car.ToStringDriver(driver)