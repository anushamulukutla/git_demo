"""
Class: Person

State: Name, Sex, Profession
Behavior: Working, Study
Using the above class, we can create multiple objects
that depict different states and behavior.

Object 1: Jessa
State:
Name: Jessa
Sex: Female
Profession: Software Engineer
Behavior:
Working: She is working as a software developer at ABC Company
Study: She studies 2 hours a day


Object 2: Jon

State:
Name: Jon
Sex: Male
Profession: Doctor
Behavior:
Working: He is working as a doctor
Study: He studies 5 hours a day

"""
#create a class
class Person:
    def __init__(self,name,sex,proffession):
        self.name= name
        self.sex=sex
        self.proffession=proffession

    def working(self):
        #print("i am in")
        print("Name:",self.name,"Sex",self.sex,"Prof",self.proffession)
        #She is working as a software developer at ABC Company

    def study(self):
        print("She is working as a :", self.proffession, "at ABC company")



jessa  = Person('anusha','female','softwareenginerr')
jon    = Person('jon','male','doctor')
#call methids
jessa.working()
jessa.study()
jon.working()
