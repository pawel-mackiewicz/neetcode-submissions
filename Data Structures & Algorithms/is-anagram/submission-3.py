class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same len
        # char in another string

        if len(s) != len(t):
            return False;

        chars = {}

        for ch in t:
            curr_val = chars.get(ch, 0)
            chars[ch] = curr_val + 1
        
#        print(chars)

        for ch in s:
            if ch in chars:
                if chars[ch] == 0:
                    return False
                chars[ch] -= 1
            else:
                return False

#        print(chars)
        return True;