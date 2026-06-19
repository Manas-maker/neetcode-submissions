class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur, seen):
            cur.append(nums[i])
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            seen.add(nums[i])
            for k in range(len(nums)):
                if nums[k] not in seen:
                    dfs(k, cur.copy(), seen.copy())
        for i in range(len(nums)): dfs(i, [], set())
        return res