#singly linked list operations

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SinglyLinkedlist:
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
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:    
            newnode.next=self.head
            self.head=newnode

    def insert_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode        
        else:
            self.tail.next=newnode
            self.tail=newnode

    
    def insert_position(self,data,pos):
        newnode=Node(data)
        if pos<1:
            print("Invalid position")
            return
        if pos==1:
            self.insert_begin(data)
            return
        count=1
        temp=self.head
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if not temp:
            print("Position out of range!")
            return
        newnode.next = temp.next
        temp.next = newnode
        if newnode.next is None:  
            self.tail = newnode    
    

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
            print("Deletion successfull")
            
    def delete_begin(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                temp = self.head
                self.head = self.head.next
                temp.next = None
            print("Deletion successfull")    

    def delete_position(self, pos):
        if pos<1:
            print("Invalid position")
            return
        if pos==1:
            self.delete_begin()
            return
        count=1
        temp=self.head
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if not temp or not temp.next:
            print("Position out of range!")
            return
        if temp.next==self.tail:
            self.delete_end()
            return
        temp.next=temp.next.next
        print("Deletion successful")
                
                
list1=SinglyLinkedlist() 

while True:
    print("1.Traversal")
    print("2.Insert begin")
    print("3.Insert end")
    print("4.Insert at position")
    print("5.Delete begin")
    print("6.Delete end")
    print("7.Delete at a position")
    print("8.Exit")
    
    try:
        n=int(input("Enter choice:"))
    except ValueError:
        print("Enter a valid integer!")
        continue
    
    if n==1:
        list1.printlist()
    elif n==2:
        data=int(input("Data:"))
        list1.insert_begin(data)
    elif n==3:
        data=int(input("Data:"))
        list1.insert_end(data)
    elif n==4:
        data=int(input("Data:"))
        pos=int(input("position:"))
        list1.insert_position(data,pos)
    elif n==5:
        list1.delete_begin()
    elif n==6:
        list1.delete_end() 
    elif n==7:
        pos=int(input("Position:"))
        list1.delete_position(pos)
    elif n==8:
        break
    else:
        print("Invalid choice")
        
        
