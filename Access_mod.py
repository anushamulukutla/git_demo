"""
1.create paretent vlass with one publicc var and protected
2.create a child cclass  emp-employee name--public and empsal--private
3.also inherit cname and proj c
4.in child class create a method show() - to displaye employee sal
5.create a ccompany objectt-and emp class object



"""
# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected#canbe  accessed with in the cclass and sub class

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.ccode)
# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here", e.name, "is working on", e._proj)
# to show the value of __sal we have created a public function show_sal()
e.show_sal()