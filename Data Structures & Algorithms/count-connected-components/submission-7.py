class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        components = n
        def find(n1):
            res = par[n1]
            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1
            return 1
        for n1, n2 in edges:
            components -= union(n1, n2)
        return components