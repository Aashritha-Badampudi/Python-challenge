'''
       Head
        │
        ▼

        n1                     n2                     n3

+------+------+------+   +------+------+------+   +------+------+------+
| Prev | Data | Next |   | Prev | Data | Next |   | Prev | Data | Next |
+------+------+------+   +------+------+------+   +------+------+------+
| None |  10  |  n2  |◄─►|  n1  |  20  |  n3  |◄─►|  n2  |  30  | None |
+------+------+------+   +------+------+------+   +------+------+------+

Implementation of node for DLL:
'''
class Node:
    def __init__(self,num):
        self.data=num
        self.next=None
        self.prev=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.next=n2
n2.next=n3
n3.next=n4

n2.prev=n1
n3.prev=n2
n4.prev=n3

print("n1 info")
print(n1,n1.data,n1.next,n1.prev)

print("n2 info")
print(n2,n2.data,n2.next,n2.prev)

print("n3 info")
print(n3,n3.data,n3.next,n3.prev)

print("n4 info")
print(n4,n4.data,n4.next,n4.prev)

