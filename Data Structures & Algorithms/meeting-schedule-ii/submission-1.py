"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        inp = []
        res = []
        for i in intervals:
            inp.append([i.start, i.end])
        inp.sort()
        for i in inp:
            if len(res)==0:
                res.append([i])
            else:
                k = 0
                while k<len(res) and res[k][-1][1]>i[0]:
                    k+=1
                if k==len(res):
                    res.append([])
                res[k].append(i)
        print(res)
        return len(res)