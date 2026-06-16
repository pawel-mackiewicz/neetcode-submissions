class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(start, end):
            rob1, rob2 = 0, 0
    
            for i in range(start, end):
                num = nums[i]
                currMax = max(rob2, rob1 + num)
                rob1 = rob2
                rob2 = currMax
            return rob2

        if len(nums) == 1:
            return nums[0]
        
        first = helper(0,len(nums)-1)
        second = helper(1,len(nums))

        return max(first,second)
        
