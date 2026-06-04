class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        ln1 = len(str1)
        ln2 = len(str2)

        def getCommonDivisors():
            res = []
            shorter = min(ln1,ln2)
            longer = max(ln1,ln2)

            divisor = shorter

            while divisor > 0:
                if shorter % divisor == 0 and longer % divisor == 0:
                    res.append(divisor)
                divisor -= 1
            
            return res

        divisors = getCommonDivisors()

        for divisor in divisors:
            sub = str1[:divisor]
            multi1 = ln1 // divisor
            multi2 = ln2 // divisor
            sub1 = ""
            sub2 = ""
            for i in range(multi1):
                sub1 += sub
            for i in range(multi2):
                sub2 += sub
            
            if sub1 == str1 and sub2 == str2:
                return sub
        
        return ""