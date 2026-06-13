class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            val = abs(num)-1

            if nums[val] < 0:
                return abs(num)
            nums[val] = -nums[val]
        
        raise Exception("invalid input")