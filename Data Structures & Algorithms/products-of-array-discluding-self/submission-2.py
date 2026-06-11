class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffixProd = [1] * len(nums) 
        for i in range(len(nums)-1, 0,-1):
            suffixProd[i-1] *= suffixProd[i] * nums[i]
        
        res = suffixProd

        prod = 1
        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]
        
        return res