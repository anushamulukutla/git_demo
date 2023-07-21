"""
what is acctually a recursion
 recursion is nothing but to repeat a func as many time as we like
 basically in python we use it using forloops  but this not only the way we can also do it with Recursion

in computer science recursion happens when a function is ccalled inside the function
    lets consider an example
    write all the positive even number small or equal to 8

    so the output should be -8 6 4 2
    and here 2 is the base case

"""
#lets define a function
def EvenNums(num):
    print(num)
    if num == 2:
        return(num)
    else:
        #calling inside the function
        return EvenNums(num-2)

EvenNums(8)
