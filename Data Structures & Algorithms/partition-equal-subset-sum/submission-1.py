class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0: return False
        target = total/2
        n = len(nums)
        def dfs(cur, curSum):
            if curSum==target:
                return True
            if cur>=n or curSum>target: return False
            return dfs(cur+1, curSum+nums[cur]) or dfs(cur+1, curSum)
        return dfs(0, 0)