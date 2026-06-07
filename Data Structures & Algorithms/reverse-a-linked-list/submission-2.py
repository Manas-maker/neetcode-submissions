# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(prev, curr):
            if not curr.next:
                curr.next = prev
                return curr
            tmpNext = curr.next
            curr.next = prev
            return reverseList(curr, tmpNext)
        return reverseList(None, head) if head else None
    