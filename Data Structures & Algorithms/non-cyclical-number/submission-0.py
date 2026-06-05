class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def f(n):
            if n == 1:
                return True
            if n in seen:
                return False
            
            seen.add(n)
            sum = 0
            while n > 0:
                a = n % 10
                n = n // 10
                sum += a**2
            
            return f(sum)

        return f(n)