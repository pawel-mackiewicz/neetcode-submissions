class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        grid = [[0] * (len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]

        grid[ROWS-1][COLS-1] = 1 if obstacleGrid[ROWS-1][COLS-1] == 0 else 0

        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if r == ROWS-1 and c == COLS-1:
                    continue
                
                right = grid[r][c+1]
                down = grid[r+1][c]

                grid[r][c] = right + down if obstacleGrid[r][c] == 0 else 0

        return grid[0][0]