class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Lsum, Rsum = 0, sum(nums)

        for i, val in enumerate(nums):
            Rsum -= val
            if Rsum == Lsum:
                return i
            Lsum += val

        return -1