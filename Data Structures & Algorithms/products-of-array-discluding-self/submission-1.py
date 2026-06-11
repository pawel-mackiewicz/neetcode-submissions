class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixSum = [1 for _ in range(len(nums))]
        suffixSum = [1 for _ in range(len(nums))]

        for i in range(1,len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, 0,-1):
            suffixSum[i-1] *= suffixSum[i] * nums[i]
        
        res = []

        for preSum, sufSum in zip(prefixSum, suffixSum):
            res.append(preSum * sufSum)
        
        return res