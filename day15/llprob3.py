#Finding the last node and adding the new node
class Node:
    def __init__(self,num):
        self.data=num
        self.add=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n1.add=n2
n2.add=n3
n3.add=n4
head=n1
tc=head
while tc.add is not None:
    tc=tc.add
tc.add=n5

head=n1
tc=head
while tc!=None:
    print(tc.data,end="-->")
    tc=tc.add