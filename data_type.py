"""
Numeric Types:	int, float, complex

Python does not have a random() function to make a random number,
but Python has a built-in module called random that can be used to make random numbers:


"""
import random
#declare a variable
num=10
num2=20.7
num3=1j
res=num+num2
print("The result is:",res)
#now get the data type of num and num2
print(type(num))
print(type(num2))
print(type(num3))
num4 =int(20)
print(num4)
#type conversion
X=10
print("X is",type(X))
#Now lets convert int x to float

a=float(X)
print("Type of a ",type(a))
#convert from int to complex:
c = complex(X)
print("c is ",type(c))
""" 
#conver complex to int

d=int(num3)
print("d",type(d))
output:
d=int(num3)
TypeError: can't convert complex to int

"""
#to get random numbers
print(random.randrange(1,1000))


#ccasting float to int ,int to int and str to int

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#casting for float

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#casting str
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
