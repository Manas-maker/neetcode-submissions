class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = sp = prices[0]
        profits = []
        for i in prices:
            if i<bp:
                bp = i
            profits.append(i-bp)
        maxP = max(profits)
        return max(maxP, 0)