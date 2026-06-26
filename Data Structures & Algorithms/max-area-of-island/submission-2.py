class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            nonlocal area
            curArea = 0
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            q = collections.deque()
            q.append((r, c))
            grid[r][c]=0
            curArea+=1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc]==1):
                        grid[nr][nc]=0
                        curArea+=1
                        q.append((nr,nc))
            area = max(area, curArea)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    bfs(r,c)
        return area
