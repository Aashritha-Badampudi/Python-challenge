class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def add(self,num):
        new=Node(num)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def psll(self):
        if self.head is None:
            print("Data is absent")
        else:
            tc=self.head
            while tc is not None:
                print(tc.data,end="->")
                tc=tc.next
            print(" TC jumped from train")

    def cnt(self):
        c=0
        if self.head is None:
            return 0
        else:
            tc=self.head
            while tc!=None:
                tc=tc.next
                c+=1
        return c
    
t=SLL()
t.add(10)
t.add(20)
t.add(30)
t.psll()
print("Count =",t.cnt())
