class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res, curSet = [], []

        def helper(i):
            if i == len(nums):
                res.append(curSet.copy())
                return

            #include
            curSet.append(nums[i])
            helper(i+1)

            #skip
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            curSet.pop()
            helper(i+1)

        helper(0)

        return res