class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res = []
        for i in intervals:
            if len(res)==0 or i[0]>res[-1][1]:
                res.append(i)
            elif i[0]<=res[-1][1]:
                res[-1] = [min(i[0], res[-1][0]), max(i[1], res[-1][1])]
        return res
                        