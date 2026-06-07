# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        stack = []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow.next:
            stack.append(slow.next)
            slow.next = slow.next.next
        newPt = head
        while len(stack)>0:
            i = stack.pop()
            tmp = newPt.next
            newPt.next = i
            i.next = tmp
            newPt = newPt.next.next