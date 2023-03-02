queue=[]
def enqueue():
    element = input("enter element")
    queue.append(element)
    print(element,"is added in q")

def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)

def display():
    print(queue)

while True:
    print("select operation 1.add 2.Remove 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        ("please enter correct operation")
        
