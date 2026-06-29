#Iterative solution
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        stack = [(None, 0)]
        seen = set()
        if len(edges)!=n-1: return False
        mappings = [[] for _ in range(n)]
        for a, b in edges:
            mappings[a].append(b)
            mappings[b].append(a)
        prev = cur = None
        while stack:
            prev, cur = stack.pop()
            if cur in seen: return False
            seen.add(cur)
            for nei in mappings[cur]:
                if nei!=prev:
                    stack.append((cur, nei))
        return len(seen)==n