class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        available, target = 0, 0
        n = len(cost)
        diff = [0]*n
        if sum(gas)<sum(cost): return -1
        run, last = 0, 0
        for i in range(n):
            run += gas[i]-cost[i]
            if run<0:
                run = 0
                last = i+1
        return last
        