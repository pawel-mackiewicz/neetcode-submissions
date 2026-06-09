class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        k = 0

        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
                count = 0
            elif count == 0:
                count = 1
                k += 1
                nums[k] = nums[i]
        return k+1