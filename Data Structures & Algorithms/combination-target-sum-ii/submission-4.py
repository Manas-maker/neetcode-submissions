class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        cur = []
        def dfs(i, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            elif i>=len(candidates) or remaining<0:
                return
            cur.append(candidates[i])
            dfs(i+1, remaining-candidates[i])
            while i<len(candidates)-1 and candidates[i+1]==candidates[i]:
                i+=1
            cur.pop()
            dfs(i+1, remaining)
        dfs(0, target)
        return res