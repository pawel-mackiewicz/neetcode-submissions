class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = nums[0]
        ln = len(nums) + 1

        L,R = 0,0

        while R < len(nums):
            if currSum >= target:
                ln = min(ln,R - L + 1)
                currSum -= nums[L]
                L += 1
            else:
                R += 1
                if R < len(nums):
                    currSum += nums[R]
        
        return ln if ln <= len(nums) else 0
