class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if nums[-1] < nums[0]:
            nums.reverse()
        
        for i in range(1,len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr < prev:
                return False

        return True