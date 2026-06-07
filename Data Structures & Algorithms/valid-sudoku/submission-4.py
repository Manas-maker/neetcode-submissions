class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if num>9 or num<1:
                        return False
                    if board[i][j] in hashmap[(0, j)]:
                        return False
                    hashmap[(0, j)].append(board[i][j])
                    if board[i][j] in hashmap[(1, i)]:
                        return False
                    hashmap[(1, i)].append(board[i][j])
                    sq = int(i/3)*3+int(j/3)
                    if board[i][j] in hashmap[(2, sq)]:
                        return False
                    hashmap[(2, sq)].append(board[i][j])
        return True
