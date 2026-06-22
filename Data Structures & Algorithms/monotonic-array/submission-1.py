class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        dec = inc = True

        # decresing check
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr > prev:
                dec = False
                break

        # incresing check
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if curr < prev:
                inc = False
                break


        return inc or dec