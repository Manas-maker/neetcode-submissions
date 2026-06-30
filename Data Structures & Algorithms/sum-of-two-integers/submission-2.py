class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            step = ((a&1)^(b&1))
            if carry:
                step = step^carry
                if step:
                    carry = 0
            if (a&1) and (b&1):
                carry = 1
            res |= step<<i
            a >>= 1
            b >>= 1
        return res if res < 0x80000000 else ~(res ^ 0xFFFFFFFF)

