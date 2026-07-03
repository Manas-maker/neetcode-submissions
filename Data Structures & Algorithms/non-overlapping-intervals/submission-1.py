class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        out = []
        count = 0
        intervals.sort()
        for i in intervals:
            if len(out)==0 or i[0]>=out[-1][1]:
                out.append(i)
            else:
                out[-1][1] = min(i[1], out[-1][1])
                count += 1
        return count