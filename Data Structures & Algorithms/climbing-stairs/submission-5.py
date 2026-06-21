class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        saves = {-1: 0, 0: 0, 1: 1, 2: 2}
        def dfs(n):
            if n in saves: return saves[n]
            saves[n] = dfs(n-1) + dfs(n-2)
            return saves[n]
        dfs(n)
        return saves[n]