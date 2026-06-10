class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height)-1
        maxLeft, maxRight = height[L], height[R]

        while L < R:
            if maxLeft < maxRight:
                res += max(maxLeft - height[L],0)
                L += 1
                maxLeft = max(maxLeft, height[L])
            else:
                res += max(maxRight - height[R],0)
                R -= 1
                maxRight = max(maxRight, height[R])

        return res