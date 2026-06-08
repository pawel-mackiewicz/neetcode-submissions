class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        count = {}

        L = 0
        for R, currChar in enumerate(s):

            currCount = count.get(currChar, 0) + 1
            count[currChar] = currCount

            maxCount = max(maxCount, currCount)

            # this mean that current window len is not valid
            if (R - L + 1) - maxCount > k:
                count[s[L]] = count[s[L]] - 1
                L += 1
                
        return R - L + 1