class DynamicArray:
    
    def __init__(self, capacity: int):
        self.data = []  
        self.capacity = capacity if capacity > 0 else 1

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() < self.capacity:
            self.data.append(n)
        else:
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        return self.data.pop()

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return len(self.data)
    
    def getCapacity(self) -> int:
        return self.capacity