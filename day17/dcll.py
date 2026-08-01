#Doubly circular linked list:
class Node:
    def __init__(self,num):
         self.data=num
         self.next=None
         self.prev=None

class dcll:
    def __init__(self):
          self.head=None

    def add_end(self,num):
        new=Node(num)
        if self.head==None:
            self.head=new
            new.next=self.head
            self.head.prev=new
        else:
            tc=self.head
            while tc.next!=self.head:
                tc=tc.next
            tc.next=new
            new.prev=tc
            new.next=self.head
            self.head.prev=new

    def pdcll(self):
        if self.head==None:
            print("Empty")
        else:
            tc=self.head
            print("from last",end="<==>")
            while tc.next is not self.head:
                print(tc.data,end="<==>")
                tc=tc.next
            print(tc.data,"<==> To first")

t=dcll()
t.add_end(20)
t.add_end(30)
t.add_end(40)
t.pdcll()