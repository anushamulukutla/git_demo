"""

Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created
 via the Person class.
Create a child class Student  which inherits from the Person class
 and which also has a section attribute.
Create a method displayStudent() that displays the name, age and
section of an object created via the Student class.
Create a student object via an instantiation on the Student class and
then test the displayStudent method.
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,name,age,section):
        self.section=section
        super(Student,self).__init__(name,age)
    def DisplayStudent(self):
        print("name:",self.name,'\n'"age:",self.age,'\n'"section:",self.section)
person1=Person("anusha",22)
person1.display()
student1=Student('anusha',22,'computer science')
student1.DisplayStudent()