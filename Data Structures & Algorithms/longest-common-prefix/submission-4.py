class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        source = strs[0]
        res = ""

        for i in range(len(source)):
            for str in strs:
                if len(str) <= i:
                    return res
                if source[i] != str[i]:
                    return res
            res += source[i]
        return res