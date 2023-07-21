


"""

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

"""

#lets check by combining one integer and string
"""  
str1 = "one pack maggie is"
str2 = 10
str_final=str1+str2
print(str_final)
#TypeError: can only concatenate str (not "int") to str

To avoid such errors we have format method in python

"""
"""   
str1 = "one pack maggie is"
#str1 = "one pack maggie is{}"
str2 = 10

print(str1.format(str2))


here we have to  givr flower braces  compulsory 
 """
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

item = "one pack maggie is {}"
value = 10
print(item.format(value))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

item="maggie "
quantity=8
price=79
order=" i want {} {} pack for {}rupees "
print(order.format(item,quantity,price))


"""
An escape character is a backslash \ followed by the character you want to insert.

The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

txt = "We are the so-called "Vikings" from the north."


    txt = "We are the so-called "Vikings" from the north."
                                 ^
SyntaxError: invalid syntax




"""
txt = "We are the so-called \"Vikings\" from the north."
#txt = "We are the so-called "Vikings" from the north."

print(txt)

#\'	Single Quote

txt='woowww ,I am glad it\'s u '
print(txt)
#
txt = "This will insert one \\ (backslash)."
print(txt)
#This will insert one \ (backslash).


txt = "Hello\nWorld!"
print(txt)

#Hello
#World!
#\r	Carriage Return
txt = "Hello\rWorld!"
print(txt)

#\t	Tab
txt = "Hello\tWorld!"
print(txt)

#\b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

#HelloWorld!
#\ooo	Octal value

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#\xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)



#
#
#
#
#
#
#








