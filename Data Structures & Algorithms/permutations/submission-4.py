class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(cur, seen):
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            for k in range(len(nums)):
                if k not in seen:
                    cur.append(nums[k])
                    seen.add(k)
                    dfs(cur, seen)
                    cur.pop()
                    seen.remove(k)
        dfs([], set())
        return res