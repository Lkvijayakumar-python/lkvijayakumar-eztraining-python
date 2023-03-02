class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while t!=None:
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print("->",end=" ")
            return
if __name__=="__main__":
    S=Stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.display()
    print(S.peek())
    S.pop()
    S.pop()
    S.display()

