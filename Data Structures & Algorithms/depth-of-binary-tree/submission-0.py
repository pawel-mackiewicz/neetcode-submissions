# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def traverse(node: TreeNode | None, curr_depth: int):
            nonlocal max_depth
            if not node:
                return
            
            max_depth = max(max_depth, curr_depth)
            traverse(node.left, curr_depth+1)
            traverse(node.right, curr_depth+1)

        traverse(root, 1)
        return max_depth