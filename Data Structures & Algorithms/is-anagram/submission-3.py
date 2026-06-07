class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        for i in s:
            if i in store:
                store[i] += 1
            else: store[i] = 1
        for i in t:
            if i in store and store[i]>0:
                if store[i] == 1: store.pop(i)
                else: store[i] -= 1
            else:
                return False
        return True if len(store) == 0 else False