class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        wholeRange = [0] * (n+1)

        for num in nums:
            wholeRange[num] = 1

        for k in range(len(wholeRange)):
            v = wholeRange[k]
            if not v:
                return k
        