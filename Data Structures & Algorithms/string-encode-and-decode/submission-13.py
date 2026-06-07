class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            enc += str(len(i))
            enc += "#"
            enc += i
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            size = ""
            j = s.index("#", i)
            size = int(s[i:j])
            i = j+1
            dec.append(s[i:i+size])
            i += size
        return dec
