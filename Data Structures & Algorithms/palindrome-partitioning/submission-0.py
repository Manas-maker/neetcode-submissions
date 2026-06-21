class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def palindromeCheck(s):
            l,r = 0, len(s)-1
            while l<=r:
                if s[l]==s[r]:
                    l += 1
                    r -= 1
                else: return False
            return True
        def dfs(s, run, cur):
            if not s:
                if palindromeCheck(run):
                    cur.append(run)
                    res.append(cur)
                return
            dfs(s[1:], run+s[0], cur.copy())
            if run and palindromeCheck(run):
                cur.append(run)
                dfs(s, '', cur.copy())
        dfs(s, '', [])
        return res
            
            

            