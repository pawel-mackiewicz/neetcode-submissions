class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)

        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for f in freq:
                if freq[f]:
                    perm.append(f)
                    freq[f] -= 1
                    dfs()
                    perm.pop()
                    freq[f] += 1
            
            return res
        
        return dfs()