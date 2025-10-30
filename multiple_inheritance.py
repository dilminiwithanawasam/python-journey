class Human():
    def __init__ (self,num_heart):
        print("calling init from Human")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("Eating")
    def work(self):
        print("Working")
class Male():
    def walk(self):
        print("Walking")
    def work(self):
        print("Male working")
class Boy(Human,Male):
    def __init__(self,name,language):
        print("calling init from Boy")
        self.name=name
        self.language=language
boy_1=Boy("John","English")
boy_1.eat()
boy_1.walk()
boy_1.work()

print(Boy.mro())