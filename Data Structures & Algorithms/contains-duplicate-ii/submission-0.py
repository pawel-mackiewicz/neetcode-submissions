class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        last_indexes = {}
        for i in range(len(nums)):
            if nums[i] in last_indexes and i - last_indexes[nums[i]] <= k:
                return True
            last_indexes[nums[i]] = i

        return False