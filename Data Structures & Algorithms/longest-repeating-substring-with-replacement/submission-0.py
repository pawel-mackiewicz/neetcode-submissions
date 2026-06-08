class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ln = 0
        mfc = s[0]
        count = {}

        L = 0
        
        for R in range(len(s)):

            currChar = s[R]
            currCount = count.get(currChar, 0) + 1
            count[currChar] = currCount

            if count[currChar] >= count[mfc]:
                mfc = currChar

            currLen = R - L + 1
            # this will mean that current window len is not valid
            if currLen - count[mfc] > k:
                count[s[L]] = count[s[L]] - 1
                L += 1
            else:
                # ln = max(ln, currLen)
                ln = currLen
                
        return ln 