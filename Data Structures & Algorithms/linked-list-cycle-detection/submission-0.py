# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash = {}
        curr = head
        while curr:
            if curr in hash:
                return True
            hash[curr] = curr.val
            curr = curr.next
        return False