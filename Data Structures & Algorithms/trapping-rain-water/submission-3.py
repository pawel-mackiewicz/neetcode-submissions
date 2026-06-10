class Solution:
    def trap(self, height: List[int]) -> int:
        # follow up - dont use arrays to store maxes - use pointers
        res = 0
        L, R = 0, len(height)-1
        maxLeft, maxRight = 0, 0

        while L < R:

            maxLeft = max(maxLeft, height[L])
            maxRight = max(maxRight, height[R])

            
            if maxLeft < maxRight:
                res += max(min(maxLeft,maxRight) - height[L],0)
                L += 1
            else:
                res += max(min(maxLeft,maxRight) - height[R],0)
                R -= 1

        return res