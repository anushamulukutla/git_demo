"""
Write a Python class named Calculator with two methods: add and add_many.
The add method should take two numbers as arguments and return their sum.
The add_many method should take any number of arguments and return their sum.


"""
class Calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=self.a+self.b
        return sum
    def add_many(self,*args):
        return sum(args)

cal=Calculator()
print(cal.add(2,3))
print(cal.add_many(1,2,3,4,5,5,6,7,7,8))


"""
Write a Python class named Person with two methods: set_name and set_age. 
The set_name method should take a string argument and set the name of the person. 
The set_age method should take an integer argument and set the age of the person.

"""
class Person:
    def set_name(self,name):
        self.name=name
        return name
    def set_age(self,age):
        self.age=age
        return age
p=Person()
print(p.set_age(45))
print(p.set_name("anu"))

