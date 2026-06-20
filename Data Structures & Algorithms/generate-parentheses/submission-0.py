class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, s, stack):
            if i==0 and not stack:
                res.append(s)
                return
            if ')' in stack:
                stack.pop()
                dfs(i, s+')', stack.copy())
                stack.append(')')
            if i>0:
                stack.append(')')
                dfs(i-1, s+'(', stack.copy())
        dfs(n, '', [])
        return res
            