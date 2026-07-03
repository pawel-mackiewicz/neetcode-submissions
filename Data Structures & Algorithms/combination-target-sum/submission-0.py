class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def helper(start, currSum):
            if currSum >= target:
                if currSum == target:
                    res.append(comb.copy())
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                helper(i, currSum+nums[i])
                comb.pop()
        
        helper(0, 0)
        return res
