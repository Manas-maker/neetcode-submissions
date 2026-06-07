class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = sp = prices[0] if len(prices)>0 else 0
        maxP = 0
        for i in prices:
            if i<bp:
                bp = i
            if (i-bp)>maxP: maxP = i-bp
        return max(maxP, 0)