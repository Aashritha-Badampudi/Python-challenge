class Node:
    def __init__(self,num):
        self.data=num
        self.add=None
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
n1.add=n2
n2.add=n3
n3.add=n4
print(n1,n1.data,n1.add)
print(n2,n2.data,n2.add)
print(n3,n3.data,n3.add)
print(n4,n4.data,n4.add)
print(n2)
print(n1.add)