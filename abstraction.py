#abstract class and abstract method in python
from abstract_class import Vehicle  
class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)
    def start(self):
        print("start with quick")
class Scooty(Vehicle):
    def __init__(self):
        super().__init__(2)
    def start(self):
        print("self start")
class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
    def start(self):
        print("start with button")
