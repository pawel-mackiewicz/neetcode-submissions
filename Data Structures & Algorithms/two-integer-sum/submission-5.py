class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        # get nums to dict{val: index}
        for i in range(len(nums)):
            val = nums[i]
            dict[val] = i

        # search for target - nums[i] in dict and return i, index
        for i in range(len(nums)):
            val = nums[i]
            searched = target - val
            if searched in dict:
                index = dict[searched]
                if index != i:
                    return [i, index]