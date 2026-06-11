class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Lsum, Rsum = 0, sum(nums)

        for i in range(len(nums)):
            Rsum -= nums[i]
            if Rsum == Lsum:
                return i
            Lsum += nums[i]

        return -1