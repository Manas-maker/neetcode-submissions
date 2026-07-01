class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        while i<n and intervals[i][1]<newInterval[0]:
            i+=1
        j=i
        while j<n and intervals[j][0]<=newInterval[1]:
            newInterval[0] = min(intervals[j][0], newInterval[0])
            newInterval[1] = max(intervals[j][1], newInterval[1])
            j+=1
        intervals[i:j] = [newInterval]
        return intervals