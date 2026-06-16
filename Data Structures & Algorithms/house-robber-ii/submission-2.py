class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def dp(i, arr, cache):
            if i >= len(arr):
                return 0
            if i in cache:
                return cache[i]
            if i == len(arr) - 1:
                return arr[i]
            
            cache[i] = max(arr[i] + dp(i+2, arr, cache), dp(i+1, arr, cache))
            return cache[i]

        first = dp(0, nums[:len(nums)-1], {})
        second = dp(0, nums[1:], {})
        return max(first, second)