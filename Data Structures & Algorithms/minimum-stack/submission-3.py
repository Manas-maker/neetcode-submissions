class MinStack:
    def __init__(self):
        self.data = []
        self.minimums = [] 

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.minimums) == 0:
            self.minimums.append(val)
        else:
            if val <= self.minimums[-1]:
                self.minimums.append(val) 
    def pop(self) -> None:
        val = self.data.pop()
        if val == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
