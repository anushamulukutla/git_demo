"""
Agends : To learn classes and Object
classes{blue print /design } and object {instance}

Syntax:
class is defined by using keyword class
class className():

object syntax
object name = classname()

how to create a method
def Method1():
how to call a method()
objectName.methodName()


"""
#example of using class and object



#create a class
#define a class
class Employee():
    #define an attribute
    employeid =0
#create an object
emp1=Employee()
emp2=Employee()
#access attribute
emp1.employeid=101
print(f"employee id is ",emp1.employeid)
emp2.employeid=102
print(f"employee id is",emp2.employeid)

# define a class
class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


