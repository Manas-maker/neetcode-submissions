class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, minProd, maxProd = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            maxMult = nums[i]*maxProd
            minMult = nums[i]*minProd
            maxProd = max(maxMult, minMult, nums[i])
            minProd = min(minMult, maxMult, nums[i])
            res = max(res, maxProd)
        return res