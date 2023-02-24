from abc import ABC,abstractmethod
class abstractdemo(ABC):
    @abstractmethod  #called decorator to
    #make the method (function)abstract one
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
# changing abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj = demo()
obj.display()
obj.show()
