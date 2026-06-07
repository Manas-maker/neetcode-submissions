class Solution:
    def checkIfPermutation(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        for i in s1:
            counts[i] += 1
        for i in s2:
            counts[i] -= 1
            if counts[i]<0:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1)-1, len(s2)):
            if (self.checkIfPermutation(s1, s2[l: r+1])):
                return True
            l+=1
        return False