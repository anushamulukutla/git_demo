"""
OOP Exercise 5: Define a property that must have the same value for every class instance (object)

"""
class Vehicle:
    colour="white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print('name:',self.name,'max_speed:',self.max_speed,'mileage',self.mileage)

class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)
        print("Colour of bus",Vehicle.colour)


class Car(Vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)
        print("colour of the car",Vehicle.colour)


vch1=Bus("BENZ",80,22)
vch2=Car("volov",70,19)




class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)