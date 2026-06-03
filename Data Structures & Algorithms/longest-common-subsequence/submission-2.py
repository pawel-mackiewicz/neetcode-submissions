class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(i, j, cache):
            txt1 = text1[i:]
            txt2 = text2[j:]

            if txt1 == "" or txt2 == "":
                return 0

            if (i,j) in cache:
                return cache[(i,j)]
            
            if txt1[0] == txt2[0]:
                cache[(i,j)] = 1 + dp(i+1, j+1,cache)
                return cache[(i,j)]
            
            
            cache[(i,j)] = max(dp(i+1,j,cache),dp(i,j+1,cache))
            return cache[(i,j)]
        
        return dp(0,0,{})