# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next
        curr, currCount = dummy, 0
        while currCount < len-n:
            curr = curr.next
            currCount += 1
        curr.next = curr.next.next
        return dummy.next