class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        islands = 0 #result

        def dfs(r,c):
            # base case
            if (
                r<0 or r>=rows or
                c<0 or c>= cols or
                grid[r][c] == "0" 
            ):
                return
            # mark visited
            grid[r][c] = "0"
            #explore neighbors
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # sequential search
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1":
                    dfs(r,c)
                    islands +=1
        return islands
        