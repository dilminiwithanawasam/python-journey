#polymorphism in classes.we can have same method in multiple classes
class Dog:
    def sound(self):
        return "Woof"
class Cat:
    def sound(self):
        return "meaw"
class Goat:
    def sound(self):
        return "ba ba"
dog=Dog()
cat=Cat()
goat=Goat()
for i in (dog,cat,goat):
    print(i.sound())