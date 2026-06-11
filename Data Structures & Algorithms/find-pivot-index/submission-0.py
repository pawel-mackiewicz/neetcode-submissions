class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Lsum, Rsum = 0, sum(nums)

        for i in range(len(nums)):
            if i > 0:
                Lsum += nums[i-1]
            Rsum -= nums[i]
            if Rsum == Lsum:
                return i

        return -1