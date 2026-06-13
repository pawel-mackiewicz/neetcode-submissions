# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        maxSum = 0

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        left, right = prev, slow
        maxSum = 0
        while right:
            maxSum = max(maxSum, left.val+right.val)
            left = left.next
            right = right.next
            
        return maxSum