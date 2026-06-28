class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        res = []
        for src, dst in prerequisites:
            inDegree[dst] += 1
            adj[src].append(dst)
        q = collections.deque()
        for n in range(numCourses):
            if inDegree[n]==0:
                q.append(n)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            res.append(node)
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return res[::-1] if finish==numCourses else []
                
        
            