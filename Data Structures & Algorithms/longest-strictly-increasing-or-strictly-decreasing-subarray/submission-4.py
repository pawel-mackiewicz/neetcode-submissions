class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        currLen = 1

        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr > prev:
                currLen += 1
            else:
                currLen = 1
            longest = max(longest, currLen)
        
        currLen = 1
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr < prev:
                currLen += 1
            else:
                currLen = 1
            longest = max(longest, currLen)

        return longest

