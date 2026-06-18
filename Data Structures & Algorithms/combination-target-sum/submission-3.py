class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, remaining):
            if remaining==0:
                res.append(subset.copy())
                return
            elif i >= len(nums) or remaining<0:
                return
            maxTimes = remaining//nums[i]
            #one time with max
            subset.extend([nums[i]]*maxTimes)
            remaining = remaining-maxTimes*nums[i]
            dfs(i+1, remaining)
            #now reducing till none are left
            for _ in range(maxTimes):
                subset.pop()
                remaining += nums[i]
                dfs(i+1, remaining)
        dfs(0, target)
        return res