class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        saves = {}
        def dfs(n):
            if n in saves: return saves[n]
            elif n<=2:
                saves[n] = n
                return n
            saves[n] = dfs(n-1) + dfs(n-2)
            return saves[n]
        dfs(n)
        return saves[n]