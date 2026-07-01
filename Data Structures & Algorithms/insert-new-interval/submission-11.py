class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if intervals[-1][1]<newInterval[0]:
            intervals.append(newInterval)
            return intervals
        for i, [start, end] in enumerate(intervals):
            if end<newInterval[0]:
                continue
            else:
                if start<=newInterval[0]:
                    if (i+1)>=len(intervals) or newInterval[1]<intervals[i+1][0]:
                        if end<newInterval[1]:
                            intervals[i][1] = newInterval[1]
                        break
                    else:
                        j=i
                        while j<len(intervals) and intervals[j][0]<=newInterval[1]: j+=1
                        if intervals[j-1][1]>=newInterval[1]:
                            intervals[i][1] = intervals[j-1][1]
                        else: intervals[i][1] = newInterval[1]
                        for k in range(j-i-1):
                            if (i+1)<len(intervals):
                                intervals.pop(i+1)
                        break
                else:
                    if newInterval[1]<start:
                        intervals.insert(i, newInterval)
                    else:
                        intervals[i][0] = newInterval[0]
                        if newInterval[1]>end:
                            j=i
                            while j<len(intervals) and intervals[j][0]<=newInterval[1]: j+=1
                            print(i, j)
                            if intervals[j-1][1]>=newInterval[1]:
                                intervals[i][1] = intervals[j-1][1]
                            else: intervals[i][1] = newInterval[1]
                            for k in range(j-i-1):
                                if (i+1)<len(intervals):
                                    intervals.pop(i+1)
                    break
        return intervals

