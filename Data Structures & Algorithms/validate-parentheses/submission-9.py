class Stack:
    def __init__(self):
        self.data = []
    def push(self, node):
        self.data.append(node)
    def pop(self):
        if len(self.data)>0:
            self.data.pop()
        else:
            return False
    def peek(self):
        if len(self.data)>0:
            return self.data[-1]
        else:
            return False
opps = {'(': ')', '{':'}', '[':']'}

class Solution:
    def isValid(self, s: str) -> bool:
        checker = Stack()
        for i in s:
            if i in opps:
                checker.push(i)
            elif checker.peek() is False:
                return False
            elif opps[checker.peek()] == i:
                checker.pop()
            else:
                return False
        return checker.peek() is False