#Single linked list
class Node:
    def __init__(self,num):
        self.data=num
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def add_end(self,num):
        new=Node(num)
        if self.head is None:
            self.head=new
        else:
            tc=self.head
            while tc.next is not None:
                tc=tc.next
            tc.next=new

    def psll(self):
        if self.head is None:
            print("Data is absent")
        else:
            tc=self.head
            while tc is not None:
                print(tc.data,end="->")
                tc=tc.next
            print(" TC jumped from train")

    def add_begin(self,num):
        new=Node(num)
        if self.head is None:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def delete_end(self):
        if self.head==None:
            print("empty")
        elif self.head.next==None:
            self.head=None
        else:
            tc=self.head
            while tc.next.next is not None:
                tc=tc.next
            tc.next=None

    #Day 16
    def insert(self,data,pos):
        new=Node(data)
        if self.head is None or pos==0:
            new.next=self.head
            self.head=new
        else:
            c=0
            tc=self.head
            pos=pos-1
            while pos!=c and tc.next!=None:
                tc=tc.next
                c+=1
            new.next=tc.next
            tc.next=new

    def delete(self,pos):
        if self.head is None:
            print("Cannot delete")
        elif pos==0:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del(temp)
        else:
            tc=self.head
            c=0
            pos=pos-1
            while tc.next!=None and c!=pos:
                tc=tc.next
                c+=1
            if c!=pos:
                print("Pos not found")
            else:
                temp=tc.next
                tc.next=temp.next
                temp.next=None
                del(temp)
t=sll()
t.add_end(10)
t.add_end(20)
t.add_end(30)
t.add_begin(50)
t.psll()
t.add_end(40)
t.psll()
t.delete_end()
t.psll()
t.insert(60,3)
t.psll()
t.insert(80,0)
t.psll()
t.delete(2)
t.psll()