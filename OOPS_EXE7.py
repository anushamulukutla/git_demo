"""
Create a Python class called BankAccount which represents a bank account, having as attributes:
accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.



"""
class BankAccount:
    def __init__(self,Accountnumber,name,balance):
        self.Accountnumber=Accountnumber
        self.name=name
        self.balance=balance
    def Deposit(self):
        print("account number =",self.Accountnumber)

    def withdrawal(self,balance):
        self.balance=balance
        currentbal=self.balance-500
        return currentbal

    def bankFees(self,fee):
        self.fee=fee
        fee=100
        bal=self.currentbal -fee
        return bal
    def display(self):
        print("Account number",self.Accountnumber)
        print("namer", self.name)
        print("bal",self.balance)
        print("ccurrent bal",self.withdrawal(self.currentbal))
        print("bal",self.bankFees(self.bal))

Bank_customer=BankAccount(56676,'nusha',3000)
Bank_customer.display()