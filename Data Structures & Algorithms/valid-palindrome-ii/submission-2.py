class Solution:
    def validPalindrome(self, s: str, deleted = False) -> bool:
        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                if deleted: 
                    return False
                return self.validPalindrome(s[left+1:right+1], True) or self.validPalindrome(s[left:right], True)
            left += 1
            right -= 1
        
        return True