class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = sp = prices[0] if len(prices)>0 else 0
        maxP = [0]*len(prices)
        for i, p in enumerate(prices):
            if i==0: continue
            if p<bp:
                bp = p
            maxP[i] = (max(maxP[i-1], p-bp))
        return maxP[-1]