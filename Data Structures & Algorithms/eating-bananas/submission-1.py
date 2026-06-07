import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<=r:
            m = (l+r)//2
            t = 0
            for i in piles:
                t += math.ceil(i/m)
            if t > h:
                l = m+1
            else:
                r = m - 1
        print(l, m, r)
        return l 