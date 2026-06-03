class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * COLS for _ in range(ROWS)]

        def dp(r,c,cache):
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c] 

            cache[r][c] = dp(r+1,c,cache) + dp(r,c+1,cache)
            return cache[r][c]

        return dp(0,0, cache)
