class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        n = len(nums)-1
        for i in range(n-1, -1, -1):
            for k in range(i+1, min(n, i+nums[i])+1):
                if dp[k]: dp[i]=True
        print(dp)
        return True if dp[0] else False