"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        newHead = Node(-1)
        newCurr = newHead
        curr = head
        while curr:
            newNode = Node(curr.val)
            newCurr.next = newNode
            hashmap[curr] = newNode
            newCurr = newNode
            curr = curr.next
        curr = head
        newCurr = newHead.next
        while curr:
            newCurr.random = hashmap[curr.random] if curr.random else None
            newCurr = newCurr.next
            curr = curr.next
        return newHead.next