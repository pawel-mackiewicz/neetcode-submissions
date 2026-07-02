class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet, res = [], []

        def helper(i):
            if i == len(nums):
                res.append(currSet.copy())
                return
            
            # include
            currSet.append(nums[i])
            helper(i+1)

            # exclude
            currSet.pop()
            helper(i+1)
        
        helper(0)

        return res