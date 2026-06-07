class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*(len(nums))
        pre, suff = 1, 1
        for i in range(len(nums)):
            out[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            out[i] *= suff
            suff *= nums[i]
        return out