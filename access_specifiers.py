class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno  # Protected attribute
        self.__age=age       # Private attribute

    def display(self):
        print((f"Hi I am {self.name}"))
# s1=Student("Alice", 1001, 20)
# print(s1.name)  # Accessing public attribute directly
#s1.display()    # Accessing public method
class Branch(Student):
    pass
b1=Branch("Bob",101,22)
print(b1.name)
print(b1._rollno)  # Accessing protected attribute from subclass
print(b1._Student__age)   # Error: Can't access private attribute

