class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = []
        dp.append(0)

        for i in range(1,n+1):
            if offset * 2 == i:
                offset *= 2
            dp.append(1 + dp[i-offset])

        return dp