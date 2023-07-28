"""
Lambda Functions in Python are anonymous functions
implying they don't have a name
For named function we use def key word
for unnamed function we use Lambda
***we can pass the fucntions to a func bcz func are obj in func
#it can take multiplt arguments
where to use it -->filter(),map(),and reduce()


LETS CONSIDER AN EXAMPLE
To find a square of a num
using the exp A*A


"""
#finding a square by using normal fucntion

def fun_square(a):

    return a*a

res=fun_square(6)
print(res)

#now lets wriete a code using lambda
#in lambda we can use only one exp
#here f is function
f = lambda a:a*a
#call f function
result=f(77)
print("using lambda",result)

"""
filter
The filter() method accepts two arguments in Python: a function and an iterable such as a list,tuple etc..
for which functions returns True...
lest see an example now..

"""
#write a example to return even numbers using filter fucntion
num=[2,4,6,7,8,9,9,20,10,22,3,33,44,5,66,7,77]

#define a function
def Even_num(num):
    if num%2==0:
        return True
    else:
        return False

even_check=filter(Even_num,num)
conver_list=list(even_check)
print(conver_list)

#using filer with lambda function
Number=[2,6,8,88,66,22,44,12,14,16,18,9]
checck_odd=list(filter(lambda Number:(Number%2!=0),Number))
print(checck_odd)

"""
Using lambda function with map()

A method and a list are passed to Python's map() function.

when ur want to change every val we can use map()
map() function returns a map object(which is an iterator) of the results after applying the given
function to each item of a given iterable (list, tuple etc.)


    
example for map()
1st filter the list with even num and 
prform Add operration using map()
 and add all the values using reduce funtion
"""


""""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
 mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.





"""

from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum)




# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
