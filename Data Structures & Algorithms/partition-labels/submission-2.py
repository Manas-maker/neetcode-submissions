class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = [-1]*26
        for i, c in enumerate(s):
            if last_seen[ord(c)-ord('a')]<i:
                last_seen[ord(c)-ord('a')] = i
        res = []
        min_last, start = 0, 0
        for i, c in enumerate(s):
            if last_seen[ord(c)-ord('a')]>min_last:
                min_last = last_seen[ord(c)-ord('a')]
            if i==min_last:
                res.append(i-start+1)
                start = i+1
        print(last_seen)
        return res