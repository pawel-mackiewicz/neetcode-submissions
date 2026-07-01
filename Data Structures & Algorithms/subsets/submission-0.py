class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, res = [], []
        
        def helper(i):
            
            if i == len(nums):
                res.append(curSet.copy())
                return

            #include
            curSet.append(nums[i])
            helper(i+1)

            #skip
            curSet.pop()
            helper(i+1)

        helper(0)

        return res