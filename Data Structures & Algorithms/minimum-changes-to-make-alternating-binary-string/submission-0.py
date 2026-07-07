class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            n = s[i]
            if i % 2 == 0:
                if n == "0":
                    count += 1
            else:
                if n == "1":
                    count += 1
        
        return min(count, len(s) - count)