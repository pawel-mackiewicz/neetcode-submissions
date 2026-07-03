class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m-1
        n = n-1
        lenOfRoad = m+n

        return math.factorial(lenOfRoad) // (math.factorial(m) * math.factorial(lenOfRoad - m))