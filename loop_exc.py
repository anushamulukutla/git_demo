"""

Exercise 1: Print First 10 natural numbers using while loop
Exercise 2: Print the following pattern
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Exercise 4: Write a program to print multiplication table of a given number
Exercise 5: Display numbers from a list using loop
The number must be divisible by five
If the number is greater than 150,
then skip it and move to the next number
If the number is greater than 500,
then stop the loop
 [12, 75, 150, 180, 145, 525, 50]
Exercise 6: Count the total number of digits in a number
Exercise 7: Print the following pattern
Exercise 8: Print list in reverse order using a loop
Exercise 9: Display numbers from -10 to -1 using for loop
Exercise 10: Use else block to display a message “Done” after successful execution of for loop
Exercise 11: Write a program to display all prime numbers within a range
Exercise 12: Display Fibonacci series up to 10 terms
Exercise 13: Find the factorial of a given number
Exercise 14: Reverse a given integer number
Exercise 15: Use a loop to display elements from a given list present at odd index positions
Exercise 16: Calculate the cube of all numbers from 1 to a given number
Exercise 17: Find the sum of the series upto n terms
Exercise 18: Print the following pattern
"""
#Print First 10 natural numbers using while loop
x=2
while (x<10):
    x=x+1
    print(x)

#sum of num

sum=0
for i in range(1,10):

    sum+=i

print("sum of all num",sum)
#Display numbers from a list using loop
list1=[1,2,3,4,5]

for i in list1:
    print(i)


#display num
list= [12, 75, 150, 180, 145, 525, 50]
for i in list:
    if(i>500):
        break
    elif(i>150):
        continue
    elif(i%5==0):
        print(i)
#Count the total number of digits in a number
#75869,
Given_num="75869"
print("given numberis ",Given_num)
print("the count of string is ",len(Given_num))

"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower than 1000,
 else return their sum.

"""
#num1=input("Enter the first number:")
#num2=input("Entre the second number:")

def func_num():
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    product=num1*num2
    if(product<=1000):
        return product
    else:
        sum=num1+num2
        return sum
res=func_num()
print(res)
