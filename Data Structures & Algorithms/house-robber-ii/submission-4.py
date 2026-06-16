class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def dp(i, end, cache):
            if i > end:
                return 0
            if i in cache:
                return cache[i]
            if i == end:
                return nums[i]
            
            cache[i] = max(nums[i] + dp(i+2, end, cache), dp(i+1, end, cache))
            return cache[i]

        first = dp(0, len(nums)-2, {})
        second = dp(1, len(nums)-1, {})
        return max(first, second)