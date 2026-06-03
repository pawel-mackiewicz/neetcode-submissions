class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(n, cache):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n-3, cache) + dp(n-2, cache) + dp(n-1, cache)
            return cache[n]
        return dp(n, {})