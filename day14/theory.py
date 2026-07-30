'''
Linked list:
- collection of nodes 
- Node: It is a combination of data and address of next node
'''

class Node:
    def __init__(self,num):
        self.data=num
        self.add=None
n1=Node(10)
print(n1)
print(n1.data)
print(n1.add)
