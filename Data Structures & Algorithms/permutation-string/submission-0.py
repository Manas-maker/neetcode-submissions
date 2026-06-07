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
        for i in range(len(s1)-1, len(s2)):
            if (self.checkIfPermutation(s1, s2[i-len(s1)+1: i+1])):
                return True
        return False