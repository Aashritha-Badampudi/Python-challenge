'''
    head
     |
     v

      n1                 n2                 n3                 n4
+-------------+    +-------------+    +-------------+    +-------------+
| data | next | -> | data | next | -> | data | next | -> | data | next |
|  10  |  n2  |    |  20  |  n3  |    |  30  |  n4  |    |  40  |  n1  |
+-------------+    +-------------+    +-------------+    +-------------+
      ^                                                           |
      |___________________________________________________________|

Implementation of the node for scll      
'''

class Node:
    def __init__(self,num):
        self.data=num
        self.next=None

class scll:
    def __init__(self):
        self.head=None

    def add_end(self,num):
        new=Node(num)
        if self.head==None:
            self.head=new
            self.head.next=new
        else:
            tc=self.head
            while tc.next!=self.head:
                tc=tc.next
            tc.next=new
            new.next=self.head

    def add_begin(self,num):
        new=Node(num)
        if self.head is None:
            self.head=new
        else:
            tc=self.head
            while tc.next!=self.head:
                tc=tc.next
            tc.next=new
            new.next=self.head
            self.head=new


    def pscll(self):
        if self.head is None:
            print("Empty")
        else:
            tc=self.head
            while tc.next is not self.head:
                print(tc.data,end="-->")
                tc=tc.next
            print(tc.data,"--> Connects to the head")

t=scll()
t.add_end(10)
t.add_end(20)
t.pscll()
t.add_begin(9)
t.pscll()
            