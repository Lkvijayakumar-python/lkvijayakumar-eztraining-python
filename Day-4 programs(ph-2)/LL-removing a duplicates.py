#LOGIC :first element will be compared with rest
#then second will be compared with be compared with rest all ..goes

class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self,ref_node):
        current = self.head
        while (current and current.next != ref_node):
               current = current.next
        return curret

    def remove(self,node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
    def display(self):
        current=self.head
        while curent:
            print(current.data,end=' ')
            current = current.next

    def remove_duplicates (a_llist):
        current1 = llist.head
        while current1 :
            data = current1.data
            current2 = current1.data
            while current2:
                if current2.data ==data:
                    llist.remove(current2)
                current2 =current2.next
            current1 =current1.next

a_llist = LinkedList()
data_list = input('please enter the element i the :').split()
for data in data_list:
    a_llist.append(int(data))
    
remove_duplicates(a_llist)

print('the list which duplicates remove::')
a_llist.display()
