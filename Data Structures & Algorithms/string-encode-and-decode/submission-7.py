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
            for j in s[i:]:
                if j == "#":
                    i += 1
                    break
                size += j
                i += 1
            size = int(size)
            dec.append(s[i:i+size])
            i += size
        return dec
