class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        if len(edges)!=n-1: return False
        visiting = set()
        mappings = [[] for _ in range(n)]
        for a, b in edges:
            mappings[a].append(b)
            mappings[b].append(a)
        def dfs(prev, cur):
            if cur in visiting:
                return False
            visiting.add(cur)
            seen.add(cur)
            for nei in mappings[cur]:
                if nei!=prev:
                    if not dfs(cur, nei): return False
            visiting.remove(cur)
            return True
        check = dfs(None, 0)
        return check and len(seen)==n

        
        