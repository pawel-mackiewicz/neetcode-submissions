class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        last_vals = set()
        for i in range(len(nums)):
            if len(last_vals) > k:
                item_to_remove = nums[i-(k+1)]
                last_vals.remove(item_to_remove)
            if nums[i] in last_vals:
                return True
            last_vals.add(nums[i])

        return False