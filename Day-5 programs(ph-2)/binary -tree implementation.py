class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

node1 = BinaryTreeNode(48)
node2 = BinaryTreeNode(7)
node3 = BinaryTreeNode(18)
node4 = BinaryTreeNode(41)
node5 = BinaryTreeNode(45)
node6 = BinaryTreeNode(3)
node7 = BinaryTreeNode(17)

node1.leftchild = node2
node1.rightchild = node3
node2.leftchild = node4
node2.rightchild = node5
node3.leftchild = node6
node3.rightchild = node7

print("Root node is :")
print(node1.data)

print("left child of the root node is:")
print(node1.leftchild.data)

print("right child of the root  node is :")
print(node1.rightchild.data)

print("Node is ")
print(node2.data)

print("left child of the node is:")
print(node2.leftchild.data)

print("right child  of the node is :")
print(node2.rightchild.data)

print("Node is ")
print(node3.data)

print("left child of the node is:")
print(node3.leftchild.data)

print("right child  of the node is :")
print(node3.rightchild.data)
