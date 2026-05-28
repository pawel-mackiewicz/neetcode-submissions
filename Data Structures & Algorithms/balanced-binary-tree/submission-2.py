# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        self.balanced = True

        def get_height(root: TreeNode | None):
            if not root:
                return 0

            left = get_height(root.left)
            right = get_height(root.right)

            if abs(left - right) > 1:
                self.balanced = False

            return 1 + max(left, right)
            
        get_height(root)
        return self.balanced