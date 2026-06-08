class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = 0
        L = 0
        maxLen = 1

        # [1,1,2]
        for R in range(1,len(arr)):
            val = arr[R]
            prevVal = arr[R-1]

            if val > prevVal:
                if sign != -1:
                    L = R - 1
                sign = 1
            elif val < prevVal:
                if sign != 1:
                    L = R - 1
                sign = -1
            else:
                sign = 0
                continue

            maxLen = max(maxLen, R - L + 1)       
        
        return maxLen