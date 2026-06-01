class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def f(n, cache):
            if n < 2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = f(n-1, cache) + f(n-2, cache)
            return cache[n]
        
        return f(n+1, {})