"""
uppercase
lowercase
strip()
replace
split
concatenate
"""
#upperccase
a = "Hello, World!"
print(a.upper())
#The lower() method returns the string in lower case:

a = "HELLO, World!"
print(a.lower())


#The strip() method removes any whitespace from the beginning or the end:

a = "          Hello, World! "
print(a.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#output:Jello, World!
str1="Hello beautiful"
print((str1.replace("beautiful","ugly")))
#The split() method returns a list where the text between the specified separator becomes the list items.

str1="hi, beauty aarna"
print(str1.split(","))
#['hi', ' beauty aarna']
#String Concatenation-To concatenate, or combine, two strings you can use the + operator.

str1='Python'
str2=' is easy'
str_final=str1 + str2
print("concatenated string is :",str_final)

str1='Python'
str2=' is easy'
str_final=str1 + "3.11" + str2
print("concatenated string is :",str_final)



