class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(l, r):
            while l>=0 and r<len(s):
                nonlocal count
                if s[l]==s[r]:
                    count+=1
                    l-=1
                    r+=1
                else: return
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return count