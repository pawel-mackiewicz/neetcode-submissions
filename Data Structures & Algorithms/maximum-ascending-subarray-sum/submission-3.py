class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]

        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr > prev:
                currSum += curr
                maxSum = max(maxSum, currSum)
            else:
                currSum = curr

        return maxSum