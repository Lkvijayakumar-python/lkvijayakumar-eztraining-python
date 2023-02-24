# one base class and multiple child class
# objects should be created by child class individuals
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1 class")
class child2(parent):
    def c2show(self):
        print("child2 class")
c1 = child1()
c1.c1show()
c1.pdisplay()
c2 = child2()
c2.c2show()
c2.pdisplay()
