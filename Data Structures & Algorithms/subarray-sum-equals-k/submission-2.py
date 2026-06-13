class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # check each subarray sum start: 0 end: i
        # check if currSum - k is in hashmap
            # if so - add count to res
        # save to hashmap -> currSum: count
            
        res = 0
        sumCount = {0:1}

        preSum = 0
        for num in nums:
            preSum += num
            res += sumCount.get(preSum - k, 0)
            sumCount[preSum] = sumCount.get(preSum, 0) + 1
        
        return res