class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = 0

        while sum != 1:
            sum = 0
            if n in seen:
                return False
            seen.add(n)
            while n > 0:
                a = n % 10
                n = n // 10
                sum += a**2
            n = sum
        return True