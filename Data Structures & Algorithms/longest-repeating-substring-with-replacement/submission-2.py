class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ln = 0
        mfc = s[0]
        maxCount = 0
        count = {}

        L = 0
        
        for R, currChar in enumerate(s):

            currCount = count.get(currChar, 0) + 1
            count[currChar] = currCount

            if currCount >= maxCount:
                maxCount = currCount

            currLen = R - L + 1
            # this will mean that current window len is not valid
            if currLen - maxCount > k:
                count[s[L]] = count[s[L]] - 1
                L += 1
            else:
                ln = currLen
                
        return ln 