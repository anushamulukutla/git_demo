class Name:
    cls_name="anusha"
    cls_id=12
    def display(self):
        print("name :",Name.cls_name)
        print("id",Name.cls_id)

obj1=Name()
dict=obj1.display()

#single level  inheritance:

class A:
    print("i am parent class")
class  B(A):
    print("i am child class:called after parent class as i am inherting parent class:")

obj1=B()
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#multilevel inheritance:

class A:
    print("parent class")
class B(A):
    print("i am child class B ")
class C(B):
    print("i am child class c :")
class D(C):
    print("i am child class  D")

obj1=D()
#multiple

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(WingedAnimal,Mammal):
    pass

# create an object of Bat class
b1 = Bat()

b1.winged_animal_info()

class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")

class C(B,A):
    def __init__(self):
        print("c")
        super().__init__()

cobj = C()

class A:
  #def method(self):
      pass
    #print("A.method() called")

class B:
    pass
  #def method(self):
      #print("B.method() called")

class C(A, B):
  pass

class E:
    def method(self):
        print("E.method() called")

class D(C, E):
  pass

d = D()
d.method()

a,b,c=(1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
print(c)

#3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class A:
    def __init__(self,name):
        self.name=name
    #def display(self):
        #print("self.name:",self.name)
        pass
obj=A("anusha")

#private var:
