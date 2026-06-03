class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        def dp(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if cache[r][c] != 0:
                return cache[r][c]

            
            
            cache[r][c] = dp(r+1, c, rows, cols, cache) + dp(r, c+1, rows, cols, cache)
            return cache[r][c]

        return dp(0,0,m,n,cache)

            
            