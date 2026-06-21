class Solution:
    def rob(self, nums: List[int]) -> int:
        maxTheft = [0]*len(nums)
        if len(nums)<=2:
            return max(nums)
        maxTheft[0], maxTheft[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxTheft[i] = max(maxTheft[i-2]+nums[i], maxTheft[i-1])
        return maxTheft[-1]
        