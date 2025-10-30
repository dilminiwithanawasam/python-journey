class A:
    def show(self):
        print("Class A")

class B(A):
    #def show(self):
        #print("Class B")4
        pass

class C(A):
    def display(self):
        print("Class C")
    #def show(self):
        #print("Class C")
class D(B,C ):
    pass

d = D()
d.show()
print(D.mro())