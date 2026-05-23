class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], low: int, high: int, target: int):

        if low > high:
            return -1

        pivot = math.floor((high+low)/2)

        if target < nums[pivot]:
            return self.binarySearch(nums, low, pivot-1, target)
        elif target > nums[pivot]:
            return self.binarySearch(nums, pivot+1, high, target)
        else:
            return pivot







    def getMiddleIndex(self, nums: List[int]) -> int:
        return math.floor(len(nums) / 2)
