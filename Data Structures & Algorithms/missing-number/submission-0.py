class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        wholeRange = set()
        for i in range(0, len(nums)+1):
            wholeRange.add(i)
        
        for num in nums:
            wholeRange.remove(num)
        
        return wholeRange.pop()