"""


Strings in python are surrounded by either single quotation marks, or double quotation marks.


"""
#assign str to a variable
a="hi"
print(a)
#You can assign a multiline string to a variable by using three quotes:single or double quotes

a=""" hjbccjdsgcjksdcnsjcbjsbcsjcb
v jbvjfbvdn
vjdbfvjdfvmdnjfbvndmv dfvdfvdfv"""
print(a)

#strings in Python are arrays of bytes representing unicode characters.

str1="My name is Anusha"
print(str1)
#in python str have index val start with 0
#now lets access specific index val
#here it even gives index val to space.
print(str1[5])
#to get the length of a string, use the len() function.
print(len(str1))
#To check if a certain phrase or character is present in a string, we can use the keyword in
print("is "in str1)
#if the phrase is not present
print("issss"in str1)

#slicing
#You can return a range of characters by using the slice syntax.
#syntax is

#Get the characters from position 1 to position 9
print(str1[1:9])

#Get the characters from the start to position 6
print(str1[:6])
#from specifiec start to end
print((str1[1:]))
"""
negative sclicing
"""
str2='Aarna'
print(str2[-4])
#take a look after
print(str2[-2:])

#Python has a set of built-in methods that you can use on strings.
"""
uppercase
lowercase
strip()
replace

"""