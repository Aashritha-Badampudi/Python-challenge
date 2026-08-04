'''
Binary Search Tree:
- Data stored in sorted
- Don't allow duplicates
- If root is none create a node and make it root
- If smallest add at left, if greater add at right

d=[17,15,11,19,25,29,23,7]

Binary Search Tree:

          17
         /  \
       15    19
      /        \
    11          25
   /           /  \
  7          23   29

Tree Traversal:
1. Inorder : 
   - There are 3 conditions:
     1. Node left
     2. Print
     3. Node Right
                 
2. Preorder : 
   - There are 3 conditions:
     1. Print
     2. Node left
     3. Node right

3. Postorder : 
   - There are 3 conditions
     1. root left
     2. root right
     3. print
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

n1=Node(12)
n2=Node(7)
n3=Node(6)
n4=Node(9)
n5=Node(8)
n6=Node(17)
n7=Node(16)
n8=Node(18)

root=n1
n1.left=n2
n1.right=n6
n2.left=n3
n2.right=n4
n4.left=n5
n6.left=n7
n6.right=n8

print("Inorder:")
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)

print(inorder(root))

print("Preorder:")
def preorder(node):
    if node is not None:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)

print(preorder(root))

print("Postorder:")
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=" ")

print(postorder(root))