class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        treasures = set()
        seen = set()
        r = 0
        while 0<=r<rows:
            c = 0
            while 0<=c<cols:
                if grid[r][c]==0:
                    treasures.add((r, c))
                    seen.add((r, c))
                c+=1
            r+=1
        q = collections.deque([treasure for treasure in treasures])
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if (nr, nc) in seen: continue
                if nr in range(rows) and nc in range(cols):
                    if grid[nr][nc]!=-1:
                        grid[nr][nc] = grid[r][c]+1
                        q.append((nr, nc))
                        seen.add((nr, nc))
                    else: continue
                