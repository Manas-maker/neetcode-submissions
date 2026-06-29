class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        count = 0
        for i in range(32):
            count += (n & 1<<i)>0
        return count