class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        PositiveDiag = set() #(r+c)
        NegativeDiag = set() #(r-c)
        board = [["."]* n for _ in range(n)] # creates a n x n matrix
        result = []
        def backtrack(r):
            # base case
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in PositiveDiag  or (r-c) in NegativeDiag :
                    continue
                col.add(c)
                PositiveDiag.add(r+c)
                NegativeDiag.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                col.remove(c)
                PositiveDiag.remove(r+c)
                NegativeDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)

        return result
        