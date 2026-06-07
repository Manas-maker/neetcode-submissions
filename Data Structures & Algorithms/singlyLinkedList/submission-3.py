class LinkedList:
    
    def __init__(self):
        self.data = {}
    
    def get(self, index: int) -> int:
        if index in self.data:
            return self.data[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        if len(self.data) > 0:
            for i in range(len(self.data)-1, -1, -1):
                self.data[i+1] = self.data[i]
            self.data[0] = val
        else:
            self.data[0] = val
    def insertTail(self, val: int) -> None:
        self.data[len(self.data)] = val

    def remove(self, index: int) -> bool:
        if index in self.data.keys():
            print(self.data.items())
            for i in range(index+1, len(self.data)):
                self.data[i-1] = self.data[i]
            self.data.pop(len(self.data)-1)
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        printer = []
        for i in range(len(self.data)):
            printer.append(self.data[i])
        return printer
