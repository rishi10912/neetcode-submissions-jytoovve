from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) #r//3 and c //e

        for r in range(9):
            for c in range(9):
                if board [r][c] != ".":
                    if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r//3,c//3)]):
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
        return True
        