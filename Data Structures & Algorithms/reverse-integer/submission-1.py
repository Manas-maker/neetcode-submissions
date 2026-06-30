class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        res = 0
        while x:
            if res>MAX//10 or res<int(MIN/10):
                return 0
            elif res == MAX//10 or res==int(MIN/10):
                if x>7 or x<-8: return 0
            res = res*10 + int(math.fmod(x, 10))
            x = int(x/10)
            print(res, x)
        return res