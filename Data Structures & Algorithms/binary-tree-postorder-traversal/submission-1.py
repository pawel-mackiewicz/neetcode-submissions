# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        res = []
        stack = []
        node = root

        while node or stack:
            if not node:
                node = stack.pop()
            elif node in visited:
                res.append(node.val)
                if not stack:
                    return res
                node = stack.pop()
            else:
                visited.append(node)
                stack.append(node)
                stack.append(node.right)
                node = node.left
        return res