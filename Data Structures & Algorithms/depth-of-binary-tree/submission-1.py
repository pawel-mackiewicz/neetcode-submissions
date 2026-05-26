# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node: TreeNode | None, curr_depth: int) -> int:
            if not node:
                return curr_depth-1
            
            left = traverse(node.left, curr_depth+1)
            right = traverse(node.right, curr_depth+1)
            return max(left,right)

        return traverse(root, 1)