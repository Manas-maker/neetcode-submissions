class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            res = par[n1]
            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return [n1, n2]
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
        for n1, n2 in edges:
            res = union(n1, n2)
            if res: return res