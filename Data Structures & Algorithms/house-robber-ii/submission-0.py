class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        prev0, cur0 = nums[0], max(nums[0], nums[1])
        prev1, cur1 = 0, nums[1]
        for i in range(2, len(nums)):
            if i!=len(nums)-1:
                prev0, cur0 = cur0, max(nums[i]+prev0, cur0)
            prev1, cur1 = cur1, max(nums[i]+prev1, cur1)
        return max(cur0, cur1)