class Solution:
    def countBits(self, n: int) -> List[int]:
        power = 0
        res = [0]*(n+1)
        if n<2:
            return [i for i in range(n+1)]
        res[0], res[1] = 0, 1
        for i in range(2, n+1):
            res[i] = res[i//2]+res[i%2]
        return res