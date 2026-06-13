class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         
        slow, fast = nums[0], nums[0]

        while True:

            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
            
        check = nums[0]

        while check != slow:
            check = nums[check]
            slow = nums[slow]

        return check