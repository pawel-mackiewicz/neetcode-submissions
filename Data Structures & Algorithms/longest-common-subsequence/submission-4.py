class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i, j, cache):
            if len(text1) == i or len(text2) == j:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]
            
            if text1[i] == text2[j]:
                cache[(i,j)] = 1 + dp(i+1, j+1,cache)
                return cache[(i,j)]
            
            
            cache[(i,j)] = max(dp(i+1,j,cache),dp(i,j+1,cache))
            return cache[(i,j)]
        
        return dp(0,0,{})