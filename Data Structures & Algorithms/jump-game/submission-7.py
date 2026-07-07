class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None]*len(nums)
        def dfs(i):
            if i>=len(nums): return False
            if dp[i] is not None: 
                return dp[i]
            if i==(len(nums)-1):
                dp[i]=True
                return True
            if nums[i]==0:
                dp[i] = False
                return False
            for k in range(nums[i], 0, -1):
                if (i+k)<len(nums) and dp[i+k] is not None:
                    if dp[i+k]: 
                        dp[i] = True
                        return True
                    else: continue
                if dfs(i+k):
                    dp[i]=True
                    return True
            dp[i] = False
            return False
        return dfs(0)
