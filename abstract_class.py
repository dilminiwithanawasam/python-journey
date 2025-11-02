from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,no_of_tyres):
        self.no_of_tyres = no_of_tyres
    @abstractmethod
    def start(self):
        pass