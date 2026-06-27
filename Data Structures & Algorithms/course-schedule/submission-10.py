class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqDict = {}
        states = [0] * numCourses
        for i in prerequisites:
            if i[0] not in preReqDict:
                preReqDict[i[0]] = [i[1]]
            else:
                preReqDict[i[0]].append(i[1])

        def dfs(course):
            if states[course] == 1: return False
            if states[course] == 2: return True
            states[course] = 1
            if course in preReqDict:
                for pre in preReqDict[course]:
                    if not dfs(pre): return False
            states[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True