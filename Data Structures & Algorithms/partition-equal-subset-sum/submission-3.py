class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total/2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for a in dp:
                if (a+nums[i])==target: return True
                nextDP.add(a+nums[i])
                nextDP.add(a)
            dp = nextDP
        return False