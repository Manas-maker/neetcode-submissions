class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur, seen):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            for k in range(len(nums)):
                if k not in seen:
                    cur.append(nums[k])
                    seen.add(k)
                    dfs(k, cur, seen)
                    cur.pop()
                    seen.remove(k)
        for i in range(len(nums)): dfs(i, [nums[i]], {i})
        return res