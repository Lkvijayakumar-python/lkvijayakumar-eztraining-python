# creating node-declaration &definition
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head #temp = first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp data is first node data
                temp = temp.next #establishing list
obj = singlelinkedlist()
#Node creation -initialising
n = Node("W")     # so n.data in Node class will be 10
obj.head =n      # assigning first node as head 
n1 = Node("I")
obj.head.next = n1 # next node value
n2 = Node("N")
n1.next =n2
n3 = Node("N")
n2.next =n3
n4 = Node("E")
n3.next = n4
n5 = Node("R")
n4.next = n5
obj.display()
