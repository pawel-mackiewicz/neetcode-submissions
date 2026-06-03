class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(n, cache):
            if n < 0:
                return 0
            if n == 0:
                return nums[n]
            if n in cache:
                return cache[n]
            
            cache[n] = max(nums[n] + dp(n-2, cache), dp(n-1, cache))
            return cache[n]
        
        return dp(len(nums)-1, {})