class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        available, target = 0, 0
        n = len(cost)
        total = 0
        run, last = 0, 0
        i = 0
        for g, c in zip(gas, cost):
            d = g - c
            run += d
            total += d
            i += 1
            if run<0:
                run = 0
                last = i
        return last if total>=0 else -1
        