class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def tread(i, j):
            grid[i][j]='0'
            if (i+1)<len(grid) and grid[i+1][j]=='1': tread(i+1, j)
            if (i-1)>-1 and grid[i-1][j]=='1': tread(i-1, j)
            if (j+1)<len(grid[0]) and grid[i][j+1]=='1': tread(i, j+1)
            if (j-1)>-1 and grid[i][j-1]=='1': tread(i, j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    tread(i, j)
                    islands += 1
        return islands