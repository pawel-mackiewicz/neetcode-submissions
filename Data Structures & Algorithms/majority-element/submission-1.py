class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        in_row = 0
        majority = 0

        for num in nums:
            if num != majority and  in_row == 0:
                majority = num;
                in_row += 1
            elif num != majority:
                in_row -= 1
            else:
                in_row += 1
        return majority