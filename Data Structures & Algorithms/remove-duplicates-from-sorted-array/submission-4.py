class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        uniques: set = set()

        for i in range(len(nums)):
            nums[j] = nums[i]

            if nums[i] not in uniques:
                uniques.add(nums[i])
                j += 1

        return j