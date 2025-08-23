#singly linked list operations

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"-> ", end="")
            temp=temp.next
        print(None)    
        
    def insert_begin(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:    
            newnode.next=self.head
            self.head=newnode

    def insert_end(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode        
        else:
            self.tail.next=newnode
            self.tail=newnode

    def delete_end(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                self.tail = temp
                self.tail.next = None
    
    def delete_begin(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                temp = self.head
                self.head = self.head.next
                temp.next = None
                
                
list1=singly_linkedlist() 

while True:
    print("1.Traversal")
    print("2.Insert begin")
    print("3.Insert end")
    print("4.Delete begin")
    print("5.Delete end")
    print("6.Exit")
    n=int(input("Enter choice:"))
    if n==1:
        list1.printlist()
    if n==2:
        data=int(input("Data:"))
        list1.insert_begin(data)
    if n==3:
        data=int(input("Data:"))
        list1.insert_end(data)
    if n==4:
        list1.delete_begin()
    if n==5:
        list1.delete_end()        
    if n==6:
        break
        
        
