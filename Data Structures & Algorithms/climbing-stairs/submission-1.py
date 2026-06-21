class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        saves = {}
        def dfs(n):
            if n in saves: return saves[n]
            elif n<0:
                return 0
            elif n==0:
                return 1
            saves[n] = dfs(n-1) + dfs(n-2)
            return saves[n]
        dfs(n)
        print(saves)
        return saves[n]