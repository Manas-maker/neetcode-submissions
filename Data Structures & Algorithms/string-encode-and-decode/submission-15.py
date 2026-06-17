class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out += str(len(i))+"#"+i
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        print(s)
        l = 0
        while l<len(s):
            length = ""
            while s[l]!="#":
                length+=s[l]
                l+=1
            length = int(length)
            string = s[l+1:l+length+1]
            out.append(string)
            l += length+1
        return out