# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        car1 = head
        car2 = head

        while car2 and car2.next:
            car1 = car1.next
            car2 = car2.next.next
        
            if car1 == car2:
                return True 
        return False