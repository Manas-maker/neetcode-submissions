class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        target = n
        for i in range(n):
            res^=nums[i]
            target ^= i
        res ^= target
        return res