class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        # backtracking DFS function
        def backtrack(r,c,i):
            # Base Case 1 : Valid state
            if i == len(word):
                return True
            # Base Case 2: Invalid state
            if (
                r < 0 or r>= rows or
                c < 0 or c>= cols or
                board[r][c] != word[i]
            ):
                return False
            # choose
            temp =board[r][c]
            # mark visisted
            board[r][c] = "#"
            #explore neighbors
            found = (
                backtrack(r-1,c,i+1)or
                backtrack(r+1,c,i+1)or
                backtrack(r,c-1,i+1)or
                backtrack(r,c+1,i+1)
            )
            # Undo, Backtrack
            board[r][c] = temp
            return found
    
        for r in range(rows):
            for c in range(cols):
                # if true then propogate up
                if backtrack(r,c,0):
                    return True
        return False
        