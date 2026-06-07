class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.tail = self.dummyHead = ListNode(0, -1)
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            if self.tail != node:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
            return node.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            if self.tail != node:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
        else:
            if self.length < self.capacity:
                newNode = ListNode(key, value)
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = self.tail.next
                self.hashmap[key] = newNode
                self.length += 1
            else:
                leastRecent = self.dummyHead.next
                self.dummyHead.next = self.dummyHead.next.next
                if self.dummyHead.next:
                    self.dummyHead.next.prev = self.dummyHead
                newNode = ListNode(key, value)
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.hashmap[newNode.key] = newNode
                self.hashmap.pop(leastRecent.key)

