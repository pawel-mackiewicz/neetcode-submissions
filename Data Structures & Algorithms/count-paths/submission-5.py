class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        cur = 1

        for i in range(1,m):
            left = 1
            for j in range(1,n):
                cur = left + row[j]
                row[j], left = cur, cur
        
        return cur