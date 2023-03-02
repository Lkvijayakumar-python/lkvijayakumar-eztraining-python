# stack implementation using arrays:
#STACK IS LIFO- LAST IN FIRST OUT

stack = []
def push():
    element = int(input("enter the element"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("Remove element:",e)
        print(stack)

while True:
    print("select operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice ==2 :
        pop_element()
    elif choice ==3:
        break
    else:
        print("Enter the correct operation")
    
