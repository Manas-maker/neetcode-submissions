class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        res = ""
        for i in t:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        need = len(freq)
        l, r = 0, len(s)
        while l<len(s):
            if s[l] in freq:
                window = {}
                have = 0
                for k in range(l, r):
                    i = s[k]
                    if i in freq:
                        if i not in window:
                            window[i] = 1
                        else: window[i] += 1
                        if window[i] == freq[i]:
                            have += 1
                    print(have, need, l)
                    if have == need:
                        if res=="":
                            res = s[l:k+1]
                        elif len(res)>(k+1-l):
                            res = s[l:k+1]
                        #res = s[l:k+1] if res=="" else min(res, s[l:k+1])
                        break
            l += 1
        return res


