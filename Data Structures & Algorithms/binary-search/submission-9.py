class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            pivot = (high+low) // 2
            if target < nums[pivot]:
                high = pivot-1
            elif target > nums[pivot]:
                low = pivot+1
            else:
                return pivot
        return -1
