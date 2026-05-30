class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        start_color = image[sr][sc]
        def dfs(grid, r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r,c) < 0 
                or r == ROWS or c == COLS 
                or (r,c) in visit
                or grid[r][c] != start_color):
                return
            else:
                grid[r][c] = color

            visit.add((r,c))

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

            visit.remove((r,c))
        
        dfs(image, sr, sc)

        return image