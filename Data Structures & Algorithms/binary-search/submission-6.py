class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], low: int, high: int, target: int):
        while low <= high:
            pivot = math.floor((high+low)/2)
            print(f'pivot: {pivot}, high: {high}, low: {low}')
            if target < nums[pivot]:
                high = pivot-1
            elif target > nums[pivot]:
                low = pivot+1
            else:
                return pivot
        return -1
