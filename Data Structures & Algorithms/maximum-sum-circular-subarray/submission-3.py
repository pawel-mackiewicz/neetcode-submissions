class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        
        for n in nums:
            totalSum += n

            currMaxSum = max(currMaxSum,0) + n
            maxSum = max(maxSum,currMaxSum)

            currMinSum = min(currMinSum,0) + n
            minSum = min(minSum,currMinSum)

        if totalSum == minSum:
            return maxSum
        return max(maxSum, totalSum - minSum)