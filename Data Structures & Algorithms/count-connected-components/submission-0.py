class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        components = 0
        stack = []
        seen = set()
        def dfs(node):
            stack.append(node)
            seen.add(node)
            while stack:
                cur = stack.pop()
                for nei in adj[cur]:
                    if nei not in seen:
                        stack.append(nei)
                    seen.add(nei)
        while len(seen)<n:
            i = 0
            while i in seen:
                i+=1
            dfs(i)
            components += 1
        return components