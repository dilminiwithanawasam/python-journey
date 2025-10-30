class Human:
    def eat(self):
        print("Eating")
    def work(self):
        print("Working")
class Male(Human):
    def work(self):
        Human.work(self)
        print("Male working")
class Boy(Male):
    def __init__(self, name, language):
        self.name = name
        self.language = language
    def do(self):
        print("Doing", self.name, "speaking", self.language)
class Programmer(Boy):
    
    def code(self):
        print("I can write programs")
boy_1=Boy("John","English")
boy_1.eat()
boy_1.work()
boy_1.do() 
prog_1=Programmer("Alice","Python")
prog_1.code()
prog_1.do()