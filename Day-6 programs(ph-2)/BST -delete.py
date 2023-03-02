class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right= None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    elif key <node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvalueNode(Node):
    current = Node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    elif key<root.key:
        root.left = deleteNode(root.left,key)
    elif(key>root.key):
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvalueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root

root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)
print("Inorder traversal of given tree")
inorder(root)
print("\Delete 20")
root = deleteNode(root,20)
print("Inorder traversal of modified tree")
inorder(root)
print("\Delete 30")
root = deleteNode(root,30)
print("Inorder traversal of modified tree")
inorder(root)
print("\Delete 50")
root = deleteNode(root,50)
print("Inorder traversal of modified tree")
inorder(root)


       
