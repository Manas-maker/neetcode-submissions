class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        rotting = set()
        fresh = set()
        seen = set()
        time = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        r = 0
        while 0<=r<rows:
            c = 0
            while 0<=c<cols:
                if grid[r][c]==1:fresh.add((r, c))
                elif grid[r][c]==2:
                    rotting.add((r, c))
                    q.append((r, c))
                c+=1
            r+=1
        if len(fresh)==0: return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==1:
                            fresh.remove((nr, nc))
                            grid[nr][nc]=2
                            q.append((nr, nc))
            time += 1
        time -= 1
        return time if not fresh else -1