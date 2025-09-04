'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example :
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):

        dummy = ListNode(0) 
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next, first.next, second.next = second, second.next, first
            prev = first

        return dummy.next
