class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        below = [0] * COLS
        curr = 0

        for r in range(ROWS-1,-1,-1):
            right = 0
            for c in range(COLS-1,-1,-1):
                if r == ROWS-1:
                    curr = grid[r][c] + right
                elif c == COLS-1:
                    curr = grid[r][c] + below[c]
                else:
                    curr = grid[r][c] + min(below[c], right)
                below[c] = right = curr

        
        return curr

1,2,3
4,5,6

0,0,0
0,0,6