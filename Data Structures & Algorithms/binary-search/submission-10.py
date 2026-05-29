class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr: List[int], start: int, end: int) -> int:
            if start > end:
                return -1

            middleI = (start + end) // 2
            middle = arr[middleI]

            if target < middle:
                return binarySearch(arr, start, middleI-1)
            if target > middle:
                return binarySearch(arr, middleI+1, end)
            return middleI

        return binarySearch(nums, 0, len(nums)-1)