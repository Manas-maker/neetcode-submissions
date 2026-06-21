class Solution:
    def climbStairs(self, n: int) -> int:
        saves = [0]*(n+1)
        if n<=2: return n
        saves[1], saves[2] = 1, 2
        print(saves)
        for i in range(3, n+1):
            saves[i] = saves[i-1] + saves[i-2]
        return saves[n]