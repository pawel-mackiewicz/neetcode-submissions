class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            n = s[i]
            if i % 2 == 0:
                count += 1 if n == "0" else 0
            else:
                count += 1 if n == "1" else 0
        
        return min(count, len(s) - count)