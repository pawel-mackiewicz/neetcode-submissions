class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        charMap = Counter(s)

        ln = 0
        odd = 0
        for count in charMap.values():
            if count % 2 == 0:
                ln += count
            else:
                ln += count - 1
                odd = 1
        
        return ln + odd 