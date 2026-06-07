class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        ln = len(nums) + 1

        L = 0

        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                ln = min(ln,R - L + 1)
                currSum -= nums[L]
                L += 1
        
        return ln if ln <= len(nums) else 0
