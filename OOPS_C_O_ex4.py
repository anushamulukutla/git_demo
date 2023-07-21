"""
Write a Rectangle class in Python language,
 allowing you to build a rectangle with length and width attributes.

Create a Perimeter() method to calculate the perimeter of the rectangle
and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width,
perimeter and area of an object created using an instantiation on rectangle class.

Create a Parallelepipede child class inheriting from the Rectangle class and
with a height attribute and another Volume() method to calculate the volume
 of the Parallelepiped.




"""
#define class
class Rectangle:
#constructor with attributes
    def __init__(self,length,width):
        self.length=length
        self.width=width
    #method parimeter
    def perimeter(self):
        perimeter=2*(self.length+self. width)
        return perimeter
        #print("Perimeter if the Rectangel :",perimeter)
#method area
    def Area(self):
        area=self.length*self.width
        return area
#method display
    def display(self):
        print("perimeter of the rectangle",self.perimeter())
        print("area of the rectangle",self.Area())
    #parallelpiped inherits Rectangle
class Parallelepiped(Rectangle):
    def __init__(self, height , length , width):
        #R().__init__(self.length, self.width)
        super().__init__(length,width)
        #super(Parallelepiped,self).__init__(length,width)
        self.height = height

    def Volume(self):
        volume=self.width*self.height*self.length
        return volume
#create an object
myrectangle=Rectangle(20,2)
#print(myrectangle)
myrectangle.display()
myparallelpiped=Parallelepiped(20,2,2)
print("volume:",myparallelpiped.Volume())

