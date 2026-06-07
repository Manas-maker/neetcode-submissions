class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        longest = 0
        seenChars = {}
        while r<len(s):
            while s[r] in seenChars:
                seenChars.pop(s[l])
                l+=1
            else:
                seenChars[s[r]] = s[r]
                r+=1
            longest = max(r-l, longest)
        print(seenChars)
        return longest
