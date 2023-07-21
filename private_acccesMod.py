"""


private:can be accesisable with in the class

"""

#define a class
class emp:
    def __init__(self,name,sal):
        self.__name=name
        self.__sal=sal
        #access private var with in the class
        print("name of the employee:",self.__name)
        print("sal of the employee",self.__sal)

#create an objecct
emp1=emp("anusha","80kcad")
#emp1.__name--->AttributeError: 'emp' object has no attribute '__name'
