class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        obstacleGrid[ROWS-1][COLS-1] = 1 if obstacleGrid[ROWS-1][COLS-1] == 0 else 0

        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if r == ROWS-1 and c == COLS-1:
                    continue
                
                right = obstacleGrid[r][c+1] if c+1 < COLS else 0
                down = obstacleGrid[r+1][c] if r+1 < ROWS else 0

                obstacleGrid[r][c] = right + down if obstacleGrid[r][c] == 0 else 0

        return obstacleGrid[0][0]