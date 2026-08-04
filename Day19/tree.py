class Node:
    def __init__(self,num):
        self.data = num
        self.left = None
        self.right = None
n1 = Node(10)
n2 = Node(15)
n3 = Node(17)
n4 = Node(16)
n5 = Node(12)
root = n1
n1.right = n3
n1.left = n2
n1.left.right = n4
n1.left.left = n5
print(root.data)
print(root.left.left.data)