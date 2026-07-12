class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        freq, window = {}, {}
        res, resLen = [-1, -1], float('inf')
        for i in t:
            freq[i] = 1 + freq.get(i, 0)
        have, need = 0, len(freq)
        l = 0
        for r in range(len(s)):
            i = s[r]
            window[i] = 1 + window.get(i, 0)
            if i in freq and window[i]==freq[i]:
                have += 1
            while have==need:
                if (r-l+1)<resLen:
                    res, resLen = (l, r), (r-l+1)
                window[s[l]] -= 1
                if s[l] in freq and window[s[l]]<freq[s[l]]:
                        have -= 1
                l += 1
        return s[res[0]:res[1]+1]




            