class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if sum(subset)==target:
                res.append(subset.copy())
                return
            elif i >= len(nums) or sum(subset)>target:
                return
            maxTimes = target//nums[i]
            #one time with max
            subset.extend([nums[i]]*maxTimes)
            dfs(i+1)

            #now reducing till none are left
            for _ in range(maxTimes):
                subset.pop()
                dfs(i+1)
        dfs(0)
        return res