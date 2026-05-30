class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        start_color = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])

        def dfs(grid, r, c):
            if (min(r,c) < 0 
                or r == ROWS or c == COLS 
                or (r,c) in visit
                or grid[r][c] != start_color):
                return

            grid[r][c] = color

            visit.add((r,c))

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

            visit.remove((r,c))
        
        dfs(image, sr, sc)

        return image