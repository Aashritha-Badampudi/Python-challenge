#Reverse linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.add=None
def rev(head):
        if head==None:
            print("Can't do")
        else:
            last=None
            prev=head.add 
            while head!=None:
                prev=head.add 
                head.add=last
                last=head
                head=prev
            head=last
        return head
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.add=n2
n2.add=n3
n3.add=n4

head=n1
head=rev(head)
tc=head
while tc!=None:
    print(tc.data,end="-->")
    tc=tc.add