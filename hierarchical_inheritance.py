#creating student child class and professor child class from person parent class using hierarchical inheritance
class Person:
    def __init__(self,firstname,lastname,age,contactNo):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.contactNo=contactNo
    def printname(self):
        print(self.firstname,self.lastname)
    def printage(self):
        print("Age:",self.age)
    def printcontact(self):
        print("Contact No:",self.contactNo)
class Student(Person):
    def __init__(self,firstname,lastname,age,contactNo,graduationyear,studentID):
        super().__init__(firstname,lastname,age,contactNo)
        self.graduationyear=graduationyear
        self.studentID=studentID
class Professor(Person):
    def __init__(self,firstname,lastname,age,contactNo,employeeID,department):
        super().__init__(firstname,lastname,age,contactNo)
        self.employeeID=employeeID
        self.department=department
student1=Student("sachini","withanawasam",22,"0712345678",2022,"S12345")
student1.printname()
student1.printage()
student1.printcontact()