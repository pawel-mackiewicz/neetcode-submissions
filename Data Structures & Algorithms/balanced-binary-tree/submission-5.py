# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(root: TreeNode | None):
            if not root:
                return 0

            left = get_height(root.left)
            if left == -1:
                return -1
            right = get_height(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return get_height(root) != -1