class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        perm = []
        res = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i-1] == nums[i] and not visited[i-1]):
                    continue
                visited[i] = True
                perm.append(nums[i])
                dfs()
                visited[i] = False
                perm.pop()


        nums.sort()
        dfs()
        return res