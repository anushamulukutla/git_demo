"""
 A collection of statements called Python Functions returns the particular task.
 By including functions, we can prevent repeating the same code block repeatedly in a program.

Python functions, once defined, can be called many times and from anywhere in a program.

If our Python program is large, it can be separated into numerous functions which is simple to track.

The key accomplishment of Python functions is we can return as many outputs as we want with different arguments.

syntax:

#def is the keyword to declare fucntion
def Function_name:
#code block

Types of function
There are two types of function in Python programming:

Standard library functions - These are built-in functions in Python that are available to use.
User-defined functions - We can create our own functions based on our requirements.



"""
#write a function to add two ele
#with passing parameters

def func_add():
    a=input("enter the value of a")
    print(a)
    b=input("enter val of b")
    print(b)
    sum=int(a) + int(b)#here int declare the ele is int type otherwise it is considerd as string and concatinate
    print("Total is:",sum)
func_add()


"""
python function Arguments:
if we create a function with arguments ,we need to pass corresponding value while calling them .

"""
def func_add_arg(num1,num2):
    sum=num1+num2
    print("total :",sum)
func_add_arg(10,20.4)
#function with one argument (fname). When the function is called, we pass along a first name,
# which is used inside the function to print the full name:
def my_function(fname):
  print(fname + " pindiproli")

my_function("Ram")
my_function("Anusha")
my_function("Aarna")

"""
Number of Arguments
By default, a function must be called with the correct number of arguments. 
Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, 
not more, and not less.

"""
#example of function with two arguments and 2 return val
def My_func(fname,lname ):
    print(fname +" "+lname)

My_func('anusha',"Mulukutla")

#exp of func with 2 arg and 1 return val

#def My_func(fname,lname ):
 #   print(fname +" "+lname)
"""
My_func('anusha')
 My_func('anusha')
TypeError: My_func() missing 1 required positional argument: 'lname'
"""
# *args Arbitrary Arguments

#This way the function will receive a tuple of arguments, and can access the items accordingly:

#f the number of arguments is unknown, add a * before the parameter name:

def My_fam_fun(*Name):
    print(Name)
My_fam_fun("aarna","anusha","ram")

def My_fam(Num1,num2,num3):
    print(Num1,num2,num3)
My_fam(Num1='Anu',num2="aarna",num3="Ram")


#**kwargs

"""
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.



"""
# def person(name, **data):
#     print(name)
#     print(data)
# person('Anu',age=25,city='Mumbai',mob=9865432)


def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('Anusha',age=25,city='Mumbai',mob=9865432)

#Default Parameter Value
def Fun_clg(group="Cse"):
    print("My groupp is "+ group)


Fun_clg("ECE")
Fun_clg("EEE")
Fun_clg()
#Passing a List as an Argument
def fun_food(food):
    for x in food:
        print(x)

veggies=['aloo','chilles','tomatoe','onion']

fun_food(veggies)
#return val
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#pass statment
"""  
function definitions cannot be empty, but if you for 
    some reason have a function definition with no content, put in the pass statement to avoid getting an error.

"""
def my_fun_pass():
    pass
