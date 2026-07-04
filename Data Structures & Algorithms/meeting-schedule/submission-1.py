"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        array = []
        out = []
        for i in intervals:
            array.append([i.start, i.end])
        array.sort()
        for i in array:
            if len(out)==0 or i[0]>=out[-1][1]:
                out.append(i)
            else:
                return False
        return True
