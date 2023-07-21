"""
Create a class called BankAccount with a "protected" attribute called _balance that stores the balance of the account.
Implement methods called deposit and withdraw that add or subtract from the balance, respectively, and a method called get_balance that returns the current balance.

Create a class called Employee with a "private" attribute called __salary that stores the employee's salary.
Implement a method called get_salary that returns the salary.


"""
class BankAccount:
    def __init__(self,_bal=0):
        self._bal=_bal
    def deposit(self,dep_amount):
        self._bal=dep_amount+self._bal
        #self._bal+=dep_amount

    def withdraw(self,with_amount):

        self._bal=self._bal-with_amount
        #print("bal_after withdraw:",withdraw_amount)
    def get_bal(self):
        return self._bal
obj=BankAccount(100)
v=obj.deposit(10)
obj.withdraw(20)
balance=obj.get_bal()
print(balance)
####################################################
"""
Create a class called Employee with a "private" attribute called __salary that stores the employee's salary.
Implement a method called get_salary that returns the salary.




"""
class Employee:
    def __init__(self,__sal):
        self.__sal=__sal
    def get_sal(self):
        return self.__sal


emp=Employee(4000)
v=emp.get_sal()
print(v)