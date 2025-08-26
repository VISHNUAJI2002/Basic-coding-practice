#Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class solution():
    def remove(self,head,n):
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
            
        pos=count-n
        if pos==0:
            return head.next
        t=head
        c=0
        while t and c<pos-1:
            t=t.next
            c+=1
        if t and t.next:
            t.next=t.next.next
        return head    
