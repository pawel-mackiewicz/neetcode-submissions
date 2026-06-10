class NumArray:

    def __init__(self, nums: List[int]):
        self.preSums = []

        self.preSums.append(nums[0])
        for i in range(1,len(nums)):
                self.preSums.append(self.preSums[i-1] + nums[i])


    def sumRange(self, left: int, right: int) -> int:
        preRight = self.preSums[right]
        preLeft = self.preSums[left-1] if left > 0 else 0
        return preRight - preLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)