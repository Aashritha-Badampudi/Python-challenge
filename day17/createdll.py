class Node:
    def __init__(self,num):
        self.data=num
        self.next=None
        self.prev=None

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

    def add_begin(self,num):
        new=Node(num)
        if self.head is Node:
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def del_end(self):
        if self.head is None:
            print("Empty")
        elif self.head.next is None:
            self.head=None
        else:
            tc=self.head
            while tc.next.next is not None:
                tc=tc.next
            dlt=tc.next
            tc.next=None
            dlt.prev=None

    def del_begin(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None

    def insert_pos(self,data,pos):
        new=Node(data)
        if self.head is None or pos==0:
            new.next=self.head
            self.head=new
        else:
            c=0
            tc=self.head
            pos=pos-1
            while tc.next is not None and c!=pos:
                tc=tc.next
                c+=1
            new.prev=tc
            new.next=tc.next
            tc.next=new             

        

    def pdll(self):
        if self.head is None:
            print("Data is empty")
        else:
            tc=self.head
            while tc is not None:
                print(tc.data,end="<==>")
                tc=tc.next
            print("TC jumped from train")
    


t=dll()
t.add_end(10)
t.add_end(20)
t.add_end(30)
t.pdll()
t.add_begin(9)
t.pdll()
t.del_end()
t.pdll()
t.del_begin()
t.pdll()
t.insert_pos(11,1)
t.pdll()