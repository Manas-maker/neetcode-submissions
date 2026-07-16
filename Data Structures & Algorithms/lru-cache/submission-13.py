class ListNode:
    def __init__(self, key: int, value: int, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.nxt = nxt
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.stack = {}
        self.capacity = capacity
        self.start = None
        self.end = None

    def get(self, key: int) -> int:
        if key in self.stack:
            node = self.stack[key]
            if self.end != node:
                if node.prev:
                    node.prev.nxt = node.nxt
                else:
                    self.start = node.nxt
                node.nxt.prev = node.prev
                self.end.nxt = node
                node.prev, node.nxt, self.end = self.end, None, node
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.stack:
            self.stack[key].value = value
            self.get(key)
        elif len(self.stack)==self.capacity:
            tmp = self.start
            if tmp.nxt:
                tmp.nxt.prev = None
            else:
                self.end = None
            self.start = tmp.nxt
            del self.stack[tmp.key]
            self.put(key, value)
        elif len(self.stack) == 0:
            self.start = self.end = ListNode(key, value)
            self.stack[key] = self.start
        else:
            newNode = ListNode(key, value, prev = self.end)
            if self.end:
                self.end.nxt = newNode
                newNode.prev = self.end
            self.end = newNode
            self.stack[newNode.key] = newNode
