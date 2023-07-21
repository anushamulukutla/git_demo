#simple example for try and excepr
def div_func():
    a=int(input("Value of a :"))
    print(a)
    b=int(input("val of b"))
    print(b)
    try:
        result=a/b
        print("result",result)
    except:
        print("please check the values entered")
    else:
        print("your are logic is correct go a head")
    finally:
        print("your are at the last line of the code")
div_func()
"""
if we denominator as 0
Value of a :2
2
val of b0
0
please the the values entered
your are at the last line of the code

"""



