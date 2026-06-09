class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L, R = 0, len(heights)-1
        res = 0
        
        while L < R:
            currArea = min(heights[L], heights[R]) * (R-L)
            res = max(res,currArea)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return res