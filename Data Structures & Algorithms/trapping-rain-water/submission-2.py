class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = []
        suffixMax = []
        res = 0
        
        maxHeight = 0
        for h in height:
            maxHeight = max(maxHeight, h)
            prefixMax.append(maxHeight)
        
        maxHeight = 0
        for i in range(len(height)-1,-1,-1):
            h = height[i]
            maxHeight = max(maxHeight, h)
            suffixMax.append(maxHeight)
        suffixMax.reverse()

        for i in range(len(height)):
            waterHeight = min(prefixMax[i], suffixMax[i]) - height[i]
            res += waterHeight

        return res