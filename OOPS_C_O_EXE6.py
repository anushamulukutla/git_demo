"""


Create a child class Bus that will inherit all of the variables
and methods of the Vehicle class


error:TypeError: object.__init__() takes exactly one argument (the instance to initialize)
Your superclass doesn’t know what to do with that extra argument to __init__. In fact, your superclass doesn’t even override __init__, and just uses the top-level object.__init__. It takes no arguments except self, but you’re giving it self and x, so you get an error saying that it takes exactly one argument but you’re passing two.

The solution is to just not pass x in the super().__init__ call.

More generally, for any class, you only want to pass super().__init__ the parameters that the superclass actually wants.
 This is about cooperative inheritance: you can take more construction/initialization parameters than your base class(es) if you want, it’s just up to you to know which ones you’re supposed to pass them and which you only want for your own use

There’s nothing really specific to the generic types defined for static type checking here (assuming I’ve guessed right what you’re asking about). None of those types override object.__init__, because they don’t do any initialization. You’re not supposed to instantiate them. They’re only there for type annotations, or to be inherited from if you have a reason to do so. (I’m not sure you actually have a reason to do so here, but let’s assume you do.)

If you try to use one of these types directly, you’ll usually get a clear error:
"""
class vehicle:
    def __init__(self,com_name):
        self.com_name=com_name
class vehicle2(vehicle):
    def __init__(self,com_nam,com_name):
        super().__init__(com_name)
        self.com_nam=com_nam

class bus(vehicle2):
    def __init__(self,com_name,speed,milage,com_nam):
        #super(vehicle2).__init__(com_nam)
        super().__init__(self,com_name)
        super().__init__(self,com_nam)
        self.speed=speed
        self.milage=milage
    def show(self):
        print("com_name:",self.com_name,'\n',"speed:",self.speed,'\n',"milage:",self.milage,'\n'"com_name-2" ,self.com_nam)

#create object for bus
bus1=bus("volvo",180,16,'benz')
bus1.show()