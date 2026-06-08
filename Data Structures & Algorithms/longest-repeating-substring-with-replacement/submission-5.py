class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ln = 0
        maxCount = 0
        count = {}

        L = 0
        
        for R, currChar in enumerate(s):

            currCount = count.get(currChar, 0) + 1
            count[currChar] = currCount

            maxCount = max(maxCount, currCount)

            ln = R - L + 1
            # this mean that current window len is not valid
            if ln - maxCount > k:
                count[s[L]] = count[s[L]] - 1
                L += 1
                ln -= 1
                
        return ln 