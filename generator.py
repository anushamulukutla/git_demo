"""
generatorwill  give u iterator
 a generator is a function that returns an iterator
 that produces a sequence of values when iterated over.
 we can create a generator in using a g=fucntion
 1. instead of return we use yield.

2.yield keyword gives us values of iteraror list
 a generator is a function that returns an iterator
 that produces a sequence of values when iterated over.

 it is almost same like return return will terminate the function but yield wont

"""
def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)
print("------------------------------------")
"""
In the above example, the my_generator() generator function takes an integer n as an argument and 
produces a sequence of numbers from 0 to n-1.

The yield keyword is used to produce a value from the generator
 and pause the generator function's execution until the next value is requested.

The for loop iterates over the generator object produced by my_generator(), 
and the print statement prints each value produced by the generator.


"""
#square for top 100 using generator

def Square_num():
    # intialize n=0
    n=1
    while n<=10:

        square=n*n
        yield square
        n+=1
for i in Square_num():
    print(i)
print( '----------------------------------- ')
##using iter and next
class square_num:
    def __init__(self,max):
        self.max=0
    def __iter__(self):
       if self.max<10:
           self.max+=1
       else:
           raise StopIteration

    def __next(self):
        return self
num=square_num(3)


def gene_fun():
    yield 5
print(gene_fun().__next__())#o/p is 5
