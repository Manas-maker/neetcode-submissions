class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        l, r = 0, len(values)-1
        res = [""]
        while l<=r:
            m = (l+r)//2
            if m<len(values) and values[m][1]<=timestamp:
                if res!=[""]:
                    res = values[m] if values[m][1]>res[1] else res
                else:
                    res = values[m]
                l = m+1
            else:
                r = m-1
        print(res)
        return res[0]
