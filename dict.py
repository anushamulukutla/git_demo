

import math
"""
Python Dictionary is used to store the data in a key-value pair format.
It is the mutable data-structure.
The elements Keys and values is employed to create the dictionary.
Keys must consist of just one element.
Value can be any type such as list, tuple, integer, etc.
syntax:
Dict = {"Name": "Chris", "Age": 20}



"""
#lets see an example of dict

dict_mob={'ram':'iphone 13pro','anu':'iphone 13 ','laxmi':'iphone 11 pro','murthy':'iphone 8'}
#lets print dict
print(dict_mob)
#now get dic val
print(dict_mob.values())
#noe get specfic key val
print(dict_mob['anu'])
#another way to val with specific key
print(dict_mob.get('ram'))


#exAMPLE 2
Employee = {"Name": "David", "Age": 30, "salary":55000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])


#Adding Dictionary Values
#CREATE A DIC
dict_add={}
print("it is an empty dict ")
print(dict_add)

#lets try to add keys and val
dict_add["Roll No :1"]="anusha"
dict_add["Roll No :2"]="Ram "
dict_add["Roll No ;3"]="AArna"
#lets print dictn
print("added key and val ",dict_add)
# Adding set of values
# with a single Key
# The std_ages doesn't exist to dictionary
dict_add["std_age"]=25,35,'1.5y'
print("after adding set of val ",dict_add)
#performing del operation

Employee = {"Name": "David", "Age": 30, "salary":55000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]
print("printing the modified information ")
print(Employee)
print("Deleting the dictionary: Employee");
#del Employee
print("Lets try to print it again ");
print(Employee)
#del using pop
#The pop() method accepts the key as an argument and remove the associated value.
# Creating a Dictionary
Dict = {1: 'JavaTpoint', 2: 'Learning', 3: 'Website'}
# Deleting a key
# using pop() method
pop_key = Dict.pop(2)
print(Dict)


#ython's len() method returns the dictionary's length. Each key-value pair lengthens the string by one.
dict = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}
len(dict)
#The any() method returns True indeed if one dictionary key does have a Boolean expression of True,
# much like it does for lists and tuples

x = math.sqrt(25)
print(x)