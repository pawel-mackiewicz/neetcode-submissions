class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c) -> int:
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == 0):
                return 0
            grid[r][c] = 0

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area