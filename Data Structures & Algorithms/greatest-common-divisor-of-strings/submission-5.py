class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        ln1 = len(str1)
        ln2 = len(str2)

        divisor = math.gcd(ln1,ln2)

        sub = str1[:divisor]
        multi1 = ln1 // divisor
        multi2 = ln2 // divisor
        sub1 = sub * multi1
        sub2 = sub * multi2
        
        if sub1 == str1 and sub2 == str2:
            return sub
    
        return ""