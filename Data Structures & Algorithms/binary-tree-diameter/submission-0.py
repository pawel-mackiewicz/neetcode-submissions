# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diams = set()

        def diam(root: TreeNode | None) -> int:
            if not root:
                return -1

            left = diam(root.left) + 1
            right = diam(root.right) + 1

            diams.add(left+right)
            return max(left,right)

        diam(root)
        return max(diams)