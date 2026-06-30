class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        target = 0
        for i in range(n):
            res^=nums[i]
            target ^= i+1
        res ^= target
        return res