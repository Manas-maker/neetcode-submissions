class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else: return False
            return True
        dp = [[False]*len(s)]*len(s)
        for i in range(len(s)):
            for j in range(len(s)):
                dp[i][j] = dp[i][j] or isPalindrome(s[i:j+1])
                if dp[i][j]: longest = max(longest, s[i: j+1], key=len)
        return longest