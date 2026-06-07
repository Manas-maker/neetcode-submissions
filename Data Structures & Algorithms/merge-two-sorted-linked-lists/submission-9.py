# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        curr1, curr2 = list1, list2
        newList = None
        if curr1 and (not curr2 or curr1.val<curr2.val):
            newList = curr1
            curr1 = curr1.next
        elif curr2:
            newList = curr2
            curr2 = curr2.next
        newHead = newList
        while curr1 and curr2:
            if curr1.val<curr2.val:
                newList.next = curr1
                curr1 = curr1.next
                newList = newList.next
            else:
                newList.next = curr2
                curr2 = curr2.next
                newList = newList.next
        newList.next = curr1 if curr1 else curr2
        return newHead
            
        