# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(q: TreeNode | None, p: TreeNode | None) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def traverse(node) -> bool:
            if not node:
                return False

            if node.val == subRoot.val and isSame(node, subRoot):
                return True

            left = traverse(node.left)
            right = traverse(node.right)

            return left or right

        return traverse(root)
            

