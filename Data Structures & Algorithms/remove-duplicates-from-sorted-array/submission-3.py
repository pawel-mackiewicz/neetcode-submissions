class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        uniques: set = set()

        while i < len(nums):
            nums[j] = nums[i]

            if nums[i] not in uniques:
                uniques.add(nums[i])
                i += 1
                j += 1
            else:
                i += 1

        return j