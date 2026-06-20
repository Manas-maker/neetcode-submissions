class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, s, openCount, closedCount):
            if i==closedCount and openCount==0:
                res.append(s)
                return
            if openCount>0:
                dfs(i, s+')', openCount-1, closedCount+1)
            if closedCount<i and (openCount+closedCount)<i:
                dfs(i, s+'(', openCount+1, closedCount)
        dfs(n, '', 0, 0)
        return res
            