class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = ''
        def expand(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            oddPali = expand(i, i)
            evenPali = expand(i, i+1)
            if len(oddPali)>len(evenPali):
                if len(oddPali)>len(max): max = oddPali
            elif len(evenPali)>len(max): max = evenPali
        return max