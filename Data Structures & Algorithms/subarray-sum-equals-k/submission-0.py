class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # check each subarray sum start: 0 end: i
        # check if currSum - k is in hashmap
            # if so - add count to res
        # save to hashmap -> sum: count
            
        res = 0

        sumCount = {0:1}

        preSum = 0
        for num in nums:
            preSum += num
            if preSum - k in sumCount:
                res += sumCount[preSum - k]
            sumCount[preSum] = sumCount.get(preSum, 0) + 1
        
        return res