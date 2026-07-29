class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # i is index of word
        def backtrack(r,c,i):
            # base case 1
            if i == len(word):
                return True
            # base case 2
            if (r<0 or r>=(rows) or c<0 or c>=(cols)or board[r][c] != word[i]):
                return False
            temp = board[r][c]
            board [r][c] = '#'
            found = (backtrack(r-1,c,i+1) or
            backtrack(r+1,c,i+1) or
            backtrack(r,c-1,i+1)or
            backtrack(r,c+1,i+1))
            #undo
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
        