"""


Create a Bus class that inherits from the Vehicle class.
Give the capacity argument of Bus.seating_capacity() a default value of 50.

 f"The seating capacity of a {self.name} is {capacity} passengers"

"""
class vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print("Bus_name",self.name)
        print("max_speed",max_speed)
        print("mielage",mileage)


    def Seat_ccapacity(self,seat=50):
        self.seat=seat
        print("capacity of the vehicle",self.seat)

class bus(vehicle):
    def __init__(self,name,max_speed,mileage):
        super().__init__(name,max_speed,mileage)

    def vehicle_type(self,color,type):
        self.color=color
        self.type=type
        print("colour of the vehicle",self.color)
        print("Type of the vehicle",self.type)

v1=bus("Benz",66,16)
v1.Seat_ccapacity()
v1.vehicle_type('red','ac')
