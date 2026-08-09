class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        area = 0 #result

        def dfs(r,c):
            # base case
            if (
                r<0 or r>=rows or
                c<0 or c>= cols or
                grid[r][c] == 0 
            ):
                return 0
            # mark visited
            grid[r][c] = 0
            #explore neighbors
            return (1+dfs(r-1,c) + dfs(r+1,c)+dfs(r,c+1)+dfs(r,c-1))
        
        # sequential search
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    area = max(area,dfs(r,c))
                    
        return area
        