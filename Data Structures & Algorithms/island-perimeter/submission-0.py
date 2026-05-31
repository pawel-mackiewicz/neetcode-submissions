class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ## count free spaces
        ## margin is an free space
        ## count horizontally and diagonally

        ROWS, COLS = len(grid), len(grid[0])
        self.perimeter = 0
        visited = []

        def dfs(r,c):
            if (r,c) in visited:
                return
            if(
                r == ROWS or c == COLS
                or r < 0 or c < 0
                or grid[r][c] == 0
            ):
                self.perimeter += 1
                return
            visited.append((r,c))
            dfs(r-1,c)            
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return self.perimeter

        return -1