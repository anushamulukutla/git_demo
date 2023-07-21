"""
Exercise 1: Create a function in Python
Exercise 2: Create a function with variable length of arguments
We use variable-length arguments if we don’t know the number of arguments needed for the function in advance.
In Python, sometimes, there is a situation where we need to pass multiple arguments to the function.
Such types of arguments are called arbitrary arguments or variable-length arguments.
arbitrary positional arguments (*args)
arbitrary keyword arguments (**kwargs)


Exercise 3: Return multiple values from a function
Exercise 4: Create a function with a default argument
Exercise 5: Create an inner function to calculate the addition in the following way
Exercise 6: Create a recursive function
Exercise 7: Assign a different name to function and call it through the new name
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Exercise 9: Find the largest item from a given list




"""
#Exercise 1: Create a function in Python
#defining afunction using def keyword
def sample_func():
    pass

def person_func(name,age):
    print("name of the person",name)
    print("age of the person",age)
person_func('anusha',26)

#Create a function with variable length of arguments

def evn_func(*num):
    for i in num:
        print(i)
evn_func(11,23,12)


# Return multiple values from a function
def cal_func(num1,num2):
    add=num1+num2
    sub=num1-num2
    print(add)
    print(sub)
    return(add,sub)

cal_func(100,60)
#Create a function with a default argument
"""

def show_employee(emp_name,emp_age,emp_sal,emp_company="capgemeni"):
    emp_list=[]
    for i in emp_list:
        #print(i)
        emp_list.append(i)
    return(emp_list)
final_emplist=show_employee("anu",26,"80k")
print(final_emplist)

"""
def show_employee(emp_name,emp_age,emp_sal,emp_company="capgemeni"):
    print("emp name:",emp_name)
    print("emp age:", emp_age)
    print("emp sal:", emp_sal)
    print("emp company:",emp_company)
show_employee('anusha',26,'80k')
"""

Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it

"""
def outer_func(a,b):

    def Cal_add(a,b):
        return a+b
    add=Cal_add(a,b)
    return add+5

result=outer_func(10,6)
print(result)

"""
Recursive function -- 0 1 2 3 4 5 6 7 8 9 10
for 0 to 10 
1+2

"""
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


def even_func(num):
    list=[]
    for num in range(4,30):
        if num%2==0:
           even= list.append(num)
           print(even)
        else:
            return 0
even_func(2)
