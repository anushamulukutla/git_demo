"""
Simply moidule can be defined as a ppiece of software code that has sepcific  code ..
usally in real time world we deal with big softwares which has lots of lines of code
so if we did anything wrong it will be hard to trace and identify the bug so
here each module has seperate file which has different functionslity of the software and
which maybe seperately editable whithout touching itrher feautres or functionlityy



"""
#import module operations to perform operation
"""
when we say import module_operations (the module name should be given every time when perom any operation 
eg:
addition= Module_operation.Add_fun(a,b)
instead of doing it complex 
just add this 
from module_operations import * --->here the star indicates import all the func 

"""
#import module_operations
from module_operations import *

a=10
b=400
#sum=module_operations.add(a,b)
sum=add(a,b)
print(sum)

