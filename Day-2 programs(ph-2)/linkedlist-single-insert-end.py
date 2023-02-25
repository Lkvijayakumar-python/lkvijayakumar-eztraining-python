# creating node-declaration &definition
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

        

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
n = Node(10)     # so n.data in Node class will be 10
obj.head =n      # assigning first node as head 
n1 = Node(20)
obj.head.next = n1 # next node value
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
print("before inserting 60")
obj.display()
print("")
print("after inserting 60")
obj.insert_end(60)
obj.display()
print("")
print("after inserting 70")
obj.insert_end(70)
obj.display()

