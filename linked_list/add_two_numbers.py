'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

Example:
Input:
2 4 3
5 6 4

Output:
7 0 8

Explanation:
342 + 465 = 807
Result stored in reverse → 7 → 0 → 8
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ------------------------
# Helper Functions
# ------------------------

def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(*result)


# ------------------------
# User Input
# ------------------------

l1 = list(map(int, input("Enter first number digits (space separated): ").split()))
l2 = list(map(int, input("Enter second number digits (space separated): ").split()))

head1 = build_linked_list(l1)
head2 = build_linked_list(l2)

solution = Solution()
result = solution.addTwoNumbers(head1, head2)

print("Result:")
print_linked_list(result)
