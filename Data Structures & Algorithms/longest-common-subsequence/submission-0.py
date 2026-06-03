class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dp(text1, text2, cache):
            if text1 == "" or text2 == "":
                return 0

            if (text1,text2) in cache:
                return cache[(text1,text2)]
            
            if text1[0] == text2[0]:
                cache[(text1,text2)] = 1 + dp(text1[1:],text2[1:],cache)
                return cache[(text1,text2)]
            
            
            cache[(text1,text2)] = max(dp(text1[1:],text2,cache),dp(text1,text2[1:],cache))
            return cache[(text1,text2)]
        
        return dp(text1,text2,{})