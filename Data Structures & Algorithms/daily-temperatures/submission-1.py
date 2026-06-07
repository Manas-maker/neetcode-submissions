class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maximums = []
        out = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while maximums and temperatures[maximums[-1]] < temperatures[i]:
                j = maximums.pop()
                out[j] = i - j
            maximums.append(i)
        return out
