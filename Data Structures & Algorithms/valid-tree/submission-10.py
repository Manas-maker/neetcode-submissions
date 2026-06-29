#Iterative solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        stack = [(None, 0)]
        seen = set()
        mappings = [[] for _ in range(n)]
        for a, b in edges:
            mappings[a].append(b)
            mappings[b].append(a)
        while stack:
            prev, cur = stack.pop()
            if cur in seen: return False
            seen.add(cur)
            for nei in mappings[cur]:
                if nei!=prev:
                    stack.append((cur, nei))
        return len(seen)==n