class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flows ={}#key: [pacificBool, atlanticBool]
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(heights), len(heights[0])
        atlanticDrainers = set()
        pacificDrainers = set()
        qAtlantic = collections.deque()
        qPacific = collections.deque()
        res = []

        #adding all the drainers to their respective queues and sets
        for i in range(rows):
            atlanticDrainers.add((i, cols-1))
            qAtlantic.append((i, cols-1))
            pacificDrainers.add((i, 0))
            qPacific.append((i, 0))
        for i in range(cols):
            atlanticDrainers.add((rows-1, i))
            qAtlantic.append((rows-1, i))
            pacificDrainers.add((0, i))
            qPacific.append((0, i))
        def bfs(q, drainers):
            while q:
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<rows and
                        0<=nc<cols and
                        heights[nr][nc]>=heights[r][c] and
                        (nr, nc) not in drainers):
                        drainers.add((nr, nc))
                        q.append((nr, nc))

        bfs(qAtlantic, atlanticDrainers)
        bfs(qPacific, pacificDrainers)
        for dr, dc in atlanticDrainers:
            if (dr, dc) in pacificDrainers: res.append([dr, dc])
        return res