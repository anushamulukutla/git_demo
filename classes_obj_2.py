"""
Agenda to learn __init__

we use init to initialize variables
and therse variables are used by object we create
 advantage it will be called itself


"""
class Computer:

    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram = ram

    def config(self):
        print("config is",self.cpu,self.ram)
#passing agrumnets to the computer class
#to accept these values we have to pass the val in __init__
#as we have three parameters in __init__ but we gave 2 para when we are calling
#here we can tell that self is the objecct it will take
comp1=Computer('i5',16)
comp2=Computer('i6',8)
comp1.config()
comp2.config()