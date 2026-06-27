import sys
sys.setrecursionlimit(10000)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqDict = {}
        visited = set()
        states = [0]*numCourses
        for i in prerequisites:
            if i[0] not in preReqDict:
                preReqDict[i[0]] = [i[1]]
            else: preReqDict[i[0]].append(i[1])
        def dfs(course):
            if states[course]==1:
                return False
            if states[course]==2:
                return True
            states[course]=1
            if course in preReqDict:
                if not all(dfs(preReqDict[course][i])  for i in range(len(preReqDict[course]))): return False
            states[course]=2
            return True
        return all(dfs(i) for i in range(numCourses))