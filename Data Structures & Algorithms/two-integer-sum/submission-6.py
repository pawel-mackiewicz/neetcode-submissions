class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        # get nums to dict{val: index}
        for i in range(len(nums)):
            val = nums[i]
            searched = target - val
            if searched in dict:
                return [dict[searched], i]
            dict[val] = i
