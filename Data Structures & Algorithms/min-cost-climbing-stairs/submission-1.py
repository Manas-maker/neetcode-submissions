class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mins = {}
        mins[0], mins[1] = 0, 0
        for i in range(len(cost)-2):
            mins[i+1] = min(mins[i+1], cost[i]+mins[i])
            if (i+2) in mins:
                mins[i+2] = min(mins[i+2], cost[i]+mins[i])
            else: mins[i+2] = cost[i]+mins[i]
        return min(mins[len(cost)-1]+cost[-1], mins[len(cost)-2]+cost[-2])