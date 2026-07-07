class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        available, target = 0, 0
        n = len(cost)
        diff = [0]*n
        for i in range(n):
            diff[i] = gas[i]-cost[i]
            available += gas[i]
            target += cost[i]
        if available<target: return -1
        run, last = 0, 0
        for i in range(n):
            run += diff[i]
            if run<0:
                run = 0
                last = i+1
        return last
        