class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = 0
        L = 0
        maxLen = 1

        R = 1
        while R < len(arr):
            val = arr[R]
            prevVal = arr[R-1]

            if sign == 0:
                if val > prevVal:
                    sign = 1
                    L = R - 1
                elif val < prevVal:
                    sign = -1
                    L = R - 1
                else: 
                    R += 1
            elif sign == -1 and val > prevVal:
                sign = 1
            elif sign == 1 and val < prevVal:
                sign = -1
            else:
                sign = 0
            
            if sign != 0:
                maxLen = max(maxLen, R - L + 1)       
                R += 1
        
        return maxLen