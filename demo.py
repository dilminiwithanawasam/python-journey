class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printname(self):
        print(self.firstname,self.lastname)
person1=Person("dilmini","withanawasam")
person1.printname()
class student(Person):
    def __init__(self,firstname,lastname,graduationyear):
        super().__init__(firstname,lastname)
        self.graduationyear=graduationyear
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
student1=student("sachini","withanawasam",2022)
student1.printname()
student1.welcome()