class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seenChars = {}
        longest = 0
        for r in range(len(s)):
            if s[r] in seenChars and seenChars[s[r]]>=l:
                l = seenChars[s[r]] + 1
            seenChars[s[r]] = r
            longest = max(r-l+1, longest)
        return longest