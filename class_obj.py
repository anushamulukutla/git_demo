#define a class
class computer:
    """
    in class we declare two things
    1.attributtes(variables)
    2. behaviour(methods)

    """
    #define a method
    def config(self):
        print("i5,16gb,1tb")
#create a object
#so here we are telling that comp1 is a obj of class computer()
comp1=computer()
print(type(comp1))
comp2=computer()
#how to call the methodvfor obj comp1 r-oneway
"""
here we  are passing a parameter is ccomp1 and the compp1 is going to the self in config()
method

"""
computer.config(comp1)
computer.config(comp2)
#the other way for calling methid config
comp1.config()
comp2.config()

