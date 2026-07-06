class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run = 0
        res = nums[0]
        for i in nums:
            run = max(i, run+i)
            res = max(res, run)
        return res

