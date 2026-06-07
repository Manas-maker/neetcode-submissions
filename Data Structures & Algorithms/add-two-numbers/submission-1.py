# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pow = 0
        num1 = num2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            num1 += curr1.val * (10**pow)
            pow += 1
            curr1 = curr1.next
        pow = 0
        while curr2:
            num2 += curr2.val*(10**pow)
            pow += 1
            curr2 = curr2.next
        sumF = num1 + num2
        newCurr = newHead = ListNode(-1)
        if sumF == 0:
            return ListNode(0)
        while sumF>0:
            newNode = ListNode(sumF%10)
            sumF = sumF//10
            newCurr.next = newNode
            newCurr = newCurr.next
        return newHead.next

        