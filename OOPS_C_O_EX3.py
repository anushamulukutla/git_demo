"""
Create a child class Bus that will inherit all of the variables and methods
of the Vehicle class


"""
class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage=milage