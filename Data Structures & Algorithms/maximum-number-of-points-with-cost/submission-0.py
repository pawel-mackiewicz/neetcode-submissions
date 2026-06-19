class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])

        left = [0] * COLS
        right = [0] * COLS
        before = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                before[c] = max(left[c],right[c]) + points[r][c]

            prev = 0
            for c in range(COLS):
                left[c] = max(before[c], prev-1)
                prev = left[c]
            prev = 0
            for c in range(COLS-1,-1,-1):
                right[c] = max(before[c], prev-1)
                prev = right[c]

            
        return max(before)
