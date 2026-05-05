class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pacific,atlantic = set(),set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)] # Up,Down,Left,Right

        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if(
                    0<= nr < rows and
                    0<= nc < cols and
                    (nr,nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr,nc,visited)
        # Pacific : Top Row
        for c in range(cols):
            dfs(0,c,pacific)
        # Pacific : Left Side
        for r in range(rows):
            dfs(r,0,pacific)
        # Atlantic : Bottom
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        # Atlantic : Right
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        # retun intersection of two sets
        return list(pacific & atlantic)        