class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums) 
        for i in range(len(nums)-1, 0,-1):
            res[i-1] = res[i] * nums[i]
        
        prod = 1
        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]
        
        return res