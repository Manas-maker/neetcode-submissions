# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        newCurr = newHead = ListNode(-1)
        carry = 0
        while curr1 and curr2:
            s = curr1.val + curr2.val+carry
            print(s%10)
            newNode = ListNode(s%10)
            carry = s//10
            curr1 = curr1.next
            curr2 = curr2.next
            newCurr.next = newNode
            newCurr = newCurr.next
        while curr1:
            s = curr1.val + carry
            carry = s//10
            newNode = ListNode(s%10)
            newCurr.next = newNode
            newCurr = newCurr.next
            curr1 = curr1.next
        while curr2:
            s = curr2.val + carry
            carry = s//10
            newNode = ListNode(s%10)
            newCurr.next = newNode
            newCurr = newCurr.next
            curr2 = curr2.next
        if carry>0:
            newNode = ListNode(carry)
            newCurr.next = newNode
            newCurr = newCurr.next

        return newHead.next