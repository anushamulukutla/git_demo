"""

- Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
2 - Define a Area() method of the class which calculates the area of ​​the circle.
3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
#area=2pir
perimeter=pir^2
"""
from math import pi

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def Area(self):
        area=2*pi*self.r
        return area
    def perimeter(self):
        perimeter=pi*self.r*self.r
        return perimeter

        # form of the cercle equation
    def formEquation(self, x, y):

        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.r ** 2

        # method to test if given point blong to the circle or not
    def test_belong(self, x, y):
            if (self.formEquation(x, y) == 0):
                print("the point: (", x, y, ") belongs to the circle C")
            else:
                print("the point: (", x, y, ") does not belong to the circle C")


My_circ=Circle(1,2,1)
area =My_circ.Area()
perimeter=My_circ.perimeter()
print(area)
print(perimeter)
My_circ.test_belong(1,1)
