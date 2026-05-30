class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.curr_area = 0
        self.max_area = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if (r < 0 or c < 0
                or r == ROWS or c == COLS
                or grid[r][c] == 0):
                return
            grid[r][c] = 0

            self.curr_area += 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r,c)
                    self.max_area = max(self.max_area, self.curr_area)
                    self.curr_area = 0
        return self.max_area