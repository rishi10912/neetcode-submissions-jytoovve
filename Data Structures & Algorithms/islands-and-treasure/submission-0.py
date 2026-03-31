from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque() # stores indices of gates

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==0:
                    q.append((r,c))
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (
                        0<=nr<rows and
                        0<=nc<cols and
                        grid[nr][nc]==inf
                    ):
                        grid[nr][nc] = grid[r][c]+1
                        q.append((nr,nc))


        