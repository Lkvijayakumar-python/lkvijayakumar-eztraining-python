class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d\nName:  %s" %(self.id,self.name))


emp1 = Employee("virat",18)
emp2 = Employee("shreyas",17)


emp1.display()
emp2.display()
