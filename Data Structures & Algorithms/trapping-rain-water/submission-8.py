class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R = 0, len(height)-1
        maxLeft, maxRight = height[L], height[R]

        while L <= R:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[L])
                res += max(maxLeft - height[L],0)
                L += 1
            else:
                maxRight = max(maxRight, height[R])
                res += max(maxRight - height[R],0)
                R -= 1

        return res