from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_count = 0
        time = 0 #result
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        #sequential traversal
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count +=1
                elif grid[r][c] ==2:
                    q.append((r,c))
        if fresh_count ==0:
            return 0
        while q:
            level_size = len(q)
            rotten = False
            for _ in range(level_size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (0<= nr < rows and
                    0<=nc <cols and
                    grid[nr][nc] ==1):
                        grid[nr][nc] =2
                        q.append((nr,nc))
                        fresh_count -=1
                        rotten = True
            if rotten:
                time +=1
        return time if fresh_count ==0 else -1
                

