class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val =key

def printinorder(root):
    if root:
        # first recuur on left child
        printinorder(root.left)
        # then print the data of node
        print(root.val,end=" ")
        # now reccur on the right child
        printinorder(root.right),

def printPostorder(root):
    if root:
        # first reccur on the left child
        printPostorder(root.left)
        # now reccur on the right child
        printPostorder(root.right)
        # then print the data of node
        print(root.val,end=" "),

def printPreorder(root):
    if root:
        #first print the data of node
        print(root.val,end=" "),
        #then reccur ton the left child
        printPreorder(root.left)
        #finally reccur on the right child
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
print("PRE-ORDER:")
printPreorder(root)
print()
print("\nIN-ORDER:")
printinorder(root)
print()
print("\n,




      POST-ORDER:")
printPostorder(root)
