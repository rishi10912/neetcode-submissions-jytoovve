class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols=len(grid[0])
        inf = 2147483647

        def dfs(grid,r,c,count):
            # base case
            if (
                r<0 or r>=rows or
                c<0 or c>=cols or
                count > grid[r][c]
            ):
                return 
            # found INF
            grid[r][c] = count

            # check neighbors
            dfs(grid,r-1,c,count+1) #Up
            dfs(grid,r+1,c,count+1) #down
            dfs(grid,r,c-1,count+1) #left
            dfs(grid,r,c+1,count+1) #right
        
        # sequential traversal
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(grid,r,c,0)
        