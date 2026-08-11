class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_collection = {}
        for i, c in enumerate(s):
            if c not in idx_collection:
                idx_collection[c] = [i]
            else:
                idx_collection[c].append(i)
        start = 0
        res = []
        while start<len(s):
            final = max(idx_collection[s[start]])
            for c in idx_collection:
                c_start = min(idx_collection[c])
                if c_start>start and c_start<final:
                    final = max(max(idx_collection[c]), final)
            res.append(final-start+1)
            start = final+1
        return res

        