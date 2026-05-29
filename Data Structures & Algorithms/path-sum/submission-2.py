# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, pathSum: int = 0) -> bool:
        if not root:
            return False
        pathSum += root.val

        if not root.left and not root.right and pathSum == targetSum:
            return True

        if self.hasPathSum(root.left, targetSum, pathSum):
            return True
        if self.hasPathSum(root.right, targetSum, pathSum):
            return True
        pathSum -= root.val
        return False

