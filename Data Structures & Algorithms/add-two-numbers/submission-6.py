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
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            s = val1+val2+carry
            newNode = ListNode(s%10)
            carry = s//10
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            newCurr.next = newNode
            newCurr = newCurr.next

        return newHead.next