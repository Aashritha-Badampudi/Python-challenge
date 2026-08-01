class Node:
    def __init__(self,num):
        self.data=num
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def add_end(self,num):
        new=Node(num)
        if self.head==None:
            self.head=new
        else:
            tc=self.head
            
            while tc.next is not None:
                tc=tc.next
                tc.next=new
                new.prev=tc