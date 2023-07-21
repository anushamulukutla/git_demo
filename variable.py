


"""




variable is a name that is used for memory allocation .In python variable is also known as identifier and used to
hold a value
In python we don't need to declare a variable type because python is smart enough to get the type of the variable
variable name can be in a com of both alphabet and num but name must start with letter or undersccore


Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter.
There is no intervention of whitespace.
For example - nameOfStudent, valueOfVaraible, etc.
Pascal Case - It is the same as the Camel Case, but here the first word is also capital.
For example - NameOfStudent, etc.
Snake Case - In the snake case, Words are separated by the underscore.
For example - name_of_student, etc.


Variable Types:
1. local
lacal variables are the variables declared in side the fucntion and scope of the variable is with the
function .


2. global

global variables are the avriables deccclares outtside the function and scope .in while declaring we must give
global keyword .

Del variable:
simply use del Keyword .



"""

#example 1:
var1=10
print(var1)
#output:10
#example 2:
#redeclaring the variable
var1=2
var1=4
print(var1)
#output:4
#assigning multiple val
var1=10,20,3
print(var1)
"""

#Assigning multiple values to multiple variables:
a,b,c=5,10,15
print(a)
print(b)
print(c)
"""
#EXAMPLE for local variable
#decclaring a function
def varadd():
    var1=10
    var2=20
    var=var1+var2
    print("sum of two var:",var)
#calling function
varadd()

#output:sum of two var: 30
"""

#lets try to access the local variable out side the function 

def varadd():
    a=10
    b=20
    var=a+b
    print("sum of two var:",var)
#calling function
varadd()
print(a)

Output:

here we can see a Name error
  print(a)
NameError: name 'a' is not defined
"""
#Global variable example:
#declating a variable

a=102
print(a)

def fun_global():
    global a
    #a=100
    print("i am a global variable",a)
#call functiom
fun_global()

#del variable
"""

def Fun_del():
    a=10
    del(a)
    print("value:",a)
    #del(a)
#UnboundLocalError: local variable 'a' referenced before assignment
Fun_del()
"""
"""

#Assigning a value to x
x = 6
print(x)
# deleting a variable.
del x
print(x)
"""

"""
how to find a type of a variable :
just use  type keyword 
"""
a=123
#b="anusha"
print(type(a))
#print(type(b))
#output <class 'int'>


# printing single value
a = 5
print(a)
print((a))

#how get the address of the var
print("id:",id(a))

a = 5
b = 6
# printing multiple variables
print(a,b)  
# separate the variables by the comma
print(1, 2, 3, 4, 5, 6, 7, 8)

"""
lets take a small example 
let say a and b var have same val whcih is 10 
usually each ele have diff add right??
what if we ccopy a val to b ?
will it have diff add ?


"""
a = 20
b = 21
#now lets print address

print("a-id",id(a))
print("b-id",id(b))
"""
output:
a-id 4460305296
b-id 4460305328
now lets assign same val to the var 

"""
a = 20
b = 20
#now lets print address

print("a-id",id(a))
print("b-id",id(b))
"""
a-id 4441832336
b-id 4441832336
we can observe that both the var a nd b have same add
 
 In python if var have same data it points  to the same memory allcocation that means same address 
 and thats the reason python is memory efficient 
 
 
 
 if and a and b are cchanges val to new val 
 her data 10 is not referedby any var so in python  we have a concept of garbage collection 
 so now 10 is garbage collected later 
 

"""

#constant var



def even(n):

    if n%2==0:
        return True
    else:
        return False
print(even(3))