class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = -1
        coins.sort()
        dp = {}
        if amount==0: return 0
        def dfs(amount, coinsUsed):
            nonlocal minCoins
            if amount == 0:
                if minCoins == -1 or minCoins>coinsUsed:
                    minCoins = coinsUsed
            elif amount<coins[0]:
                return -1
            else:
                for i in  range(len(coins)-1, -1, -1):
                    if coins[i]<=amount:
                        if ((amount//coins[i]+coinsUsed)<minCoins) or minCoins==-1:
                            dfs(amount-coins[i], coinsUsed+1)
        dfs(amount, 0)
        return minCoins

