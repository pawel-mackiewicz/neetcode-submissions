# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # iterate and keep all vals in deque
        # then popleft and popright and check if maxSum
        # return maxSum

        maxSum = 0

        deq = deque()

        node = head
        while node:
            deq.append(node.val)
            node = node.next
        
        while deq:
            left = deq.popleft()
            right = deq.pop()

            maxSum = max(maxSum, left+right)
        return maxSum