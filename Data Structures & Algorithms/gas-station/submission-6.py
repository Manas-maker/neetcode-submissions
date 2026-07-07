class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        available, target = 0, 0
        n = len(cost)
        total = 0
        run, last = 0, 0
        for i in range(n):
            d = gas[i]-cost[i]
            run += d
            total += d
            if run<0:
                run = 0
                last = i+1
        return last if total>=0 else -1
        