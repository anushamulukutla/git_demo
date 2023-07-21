"""
types of function;\
builtin
user defined


Creating a function without any parameters
Creating a function with parameters
Creating a function with parameters and return value




"""
#Creating a function without any parameters
#lets create a simple func with out any parameter
#define fun
def Sample_fun():
    print("hey hai, i am a sample python function")
#calling function
Sample_fun()

#Creating a function with parameters
def person_fun(name,age):
    print(name)
    print(age)

person_fun('anusha',26)

"""

Creating a function with parameters and return value
Functions can return a value. 
The return value is the output of the function. Use the return keyword to return value from a function.


"""
def add_fun(a,b):
    add=a+b
    return add
res=add_fun(10,5)
print("addition of two val",res)

#-----------------------------docstrings------------------------------------------------------
def factorial(x):
    """This function returns the factorial of a given number."""
    return x

# access doc string
print(factorial.__doc__)
#When you use the help function to get the information of any function, it returns the docstring.
print(help(factorial))
#-----------------------------------Retturn value from  a Function----------
'''
Syntax of return statement

def fun():
    statement-1
    statement-2
    statement-3
    .          
    .          
    return [expression]
The return statement ends the function execution.
For a function, it is not mandatory to return a value.
If a return statement is used without any expression, then the None is returned.
The return statement should be inside of the function block.

'''
def is_even(list1):
    even_num=[]
    for list1 in list1:
        if list1%2==0:
            #appending val to list
            even_num.append(list1)
    return even_num
#here even_num is variable and we are passing a list to is_even
even_num=is_even([10,4,5,8,7,9])
print("even numbers:",even_num)

# Return multiple values from a function
def cal_func(num1,num2):
    add=num1+num2
    sub=num1-num2
    print(add)
    print(sub)
    return(add,sub)

cal_func(100,60)


#------------------#local variables-----------------------------
def function1():
    # local variable
    loc_var = 888
    print("Value is :", loc_var)
#here we are trying to use variable loc_var can be only used in function1

def function2():
    pass

#print("Value is :", loc_var)

function1()
function2()
#------------------#global variables-----------------------------

"""
Global Variable in function
A Global variable is a variable that declares outside of the function.
 The scope of a global variable is broad. It is accessible in all functions of the same module.

"""
global_var = 999

def function1():
    print("Value in 1nd function :", global_var)

def function2():
    print("Value in 2nd function :", global_var)

function1()
function2()
#example for modifying the global var

global_var = 5

def function1():
    print("Value in 1st function :", global_var)

def function2():
    # Modify global variable
    # function will treat it as a local variable
    global_var = 555
    print("Value in 2nd function :", global_var)

def function3():
    print("Value in 3rd function :", global_var)

function1()
function2()
function3()


x = 5

# defining 1st function
def function1():
    print("Value in 1st function :", x)

# defining 2nd function
def function2():
    # Modify global variable using global keyword
    global x
    x = 555
    print("Value in 2nd function :", x)

# defining 3rd function
def function3():
    print("Value in 3rd function :", x)

function1()
function2()
function3()


#------------------#nonlocal variables-----------------------------

"""
non local variable is a keywordused to declared a variable  as  a global var for nested functions 
We can use a nonlocal keyword when we want to declare a variable in the local scope but act as a global scope.


"""
def outer_func():
    #global variable
    x = 777
    print("hey hai  i am global var",x)

    def inner_func():
        # local variable now acts as global variable
        nonlocal x
        x = 700
        print("value of x inside inner function is :", x)

    inner_func()
    #in this function we get out put for x as 700
    print("value of x inside outer function is :", x)

outer_func()


"""
Python Function Arguments
The argument is a value, a variable, or an object that we pass to a function or method call. 
In Python, there are four types of arguments allowed.

Positional arguments
keyword arguments
Default arguments
Variable-length arguments


"""
#Positional arguments

"""
For example, A function show_employee() that accepts the employee’s name and salary and displays both. 
Let’s modify a function definition and assigned a default value 8000 to a salary. 
Next, if salary value is missing in the function call,
 the function automatically takes default value 9000 as a salary.

"""
def show_employee(name,sal=8000):
    print(name)
    print(sal)
#show_employee('anu',8000)
show_employee("anu")