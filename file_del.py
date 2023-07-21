"""


To delete a file, you must import the OS module,
and run its os.remove() function
"""
import os

file=open("an",'w')
file.write("hi this is anusha")
print("file is created")
os.remove("an")
print("file is deleted...")
#to remove entire folder
#os.rmdir("myfolder")
