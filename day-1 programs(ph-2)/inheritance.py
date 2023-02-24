# one parent and one child class
class parent:        #base class
    def display(self):
        print("parent class")

# derived class
class child(parent):     #child inherits properties
    def show(self):
        print("child class")

c = child()     #c is object for child class
c.display()
c.show()
        
