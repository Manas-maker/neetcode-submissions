# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        tail = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        nextNode = mid.next
        mid.next = None
        prev = None
        while nextNode:
            tmp = nextNode.next
            nextNode.next = prev
            prev = nextNode
            nextNode = tmp
        tail = prev
        curr = head
        while tail:
            tmp = curr.next
            curr.next = tail
            tmpBack = tail.next
            tail.next = tmp
            tail = tmpBack
            curr = curr.next.next

