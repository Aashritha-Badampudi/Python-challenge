#WAP to find the max and min elements in the linked list
class Node:
    def __init__(self,nums):
        self.data=nums
        self.add=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.add=n2
n2.add=n3
n3.add=n4

head=n1


