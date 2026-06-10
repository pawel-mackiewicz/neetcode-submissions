class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height)-1
        maxLeft, maxRight = height[L], height[R]

        while L <= R:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[L])
                res += maxLeft - height[L]
                L += 1
            else:
                maxRight = max(maxRight, height[R])
                res += maxRight - height[R]
                R -= 1

        return res