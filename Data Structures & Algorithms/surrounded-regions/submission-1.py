class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        r = 0
        q = collections.deque()
        borders = set()
        while 0<=r<rows:
            c = 0
            while 0<=c<cols:
                if (r==0 or c==0 or r==(rows-1) or c==(cols-1)) and board[r][c]=='O':
                        q.append((r, c))
                        borders.add((r, c))
                c+=1
            r+=1
        while q:
            r, c = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=='O' and (nr, nc) not in borders:
                    borders.add((nr, nc))
                    q.append((nr, nc))
        r=0
        while 0<=r<rows:
            c = 0
            while 0<=c<cols:
                if board[r][c]=='O' and (r, c) not in borders:
                    board[r][c]='X'
                c+=1
            r+=1