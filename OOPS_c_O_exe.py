"""
Write a Python program to create a Vehicle class with max_speed and mileage
instance attribute
"""
class vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage


car1=vehicle(80,12)
#orint the val
print(car1.max_speed,car1.milage)