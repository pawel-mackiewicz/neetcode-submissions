# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def calculatePathSum(node: TreeNode | None, pathSum: int) -> bool:
            if not node:
                return False
            pathSum += node.val

            if not node.left and not node.right and pathSum == targetSum:
                return True

            if calculatePathSum(node.left, pathSum):
                return True
            if calculatePathSum(node.right, pathSum):
                return True
            pathSum -= node.val
            return False

        return calculatePathSum(root, 0)
