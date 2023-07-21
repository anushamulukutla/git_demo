"""

A tuple in Python is similar to a list.
The difference between the two is that we cannot change the elements of a tuple once it is assigned
 whereas we can change the elements of a list.



tuple has two methods
count
index

"""
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
#Tuples can be constructed without using parentheses. This is known as triple packing.

# Python program to create a tuple without using parentheses
# Creating a tuple
tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]
# Displaying the tuple created
print(tuple_)
# Checking the data type of object tuple_
print(type(tuple_) )
# Trying to modify tuple_
try:
    tuple_[1] = 4.2
except:
    print(TypeError )

#if we have  only one element in the tuple in the double quote is string..
single_tuple = ("Tuple")
print( type(single_tuple) )
# Creating a tuple that has only one element
single_tuple = ("Tuple",)
print( type(single_tuple) )
# Creating tuple without parentheses
single_tuple = "Tuple",
print( type(single_tuple) )
#
tuple_.count()
print(tuple_)