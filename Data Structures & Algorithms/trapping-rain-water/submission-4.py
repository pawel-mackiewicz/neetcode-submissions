class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height)-1
        maxLeft, maxRight = 0, 0

        while L < R:

            maxLeft = max(maxLeft, height[L])
            maxRight = max(maxRight, height[R])
            
            if maxLeft < maxRight:
                res += max(maxLeft - height[L],0)
                L += 1
            else:
                res += max(maxRight - height[R],0)
                R -= 1

        return res