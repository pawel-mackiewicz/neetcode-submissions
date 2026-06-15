# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def getLen(node, cache):
            if not node:
                return 0
            if node in cache:
                return cache[node]

            left = getLen(node.left, cache)
            right = getLen(node.right, cache)
            self.maxDiam = max(self.maxDiam, left + right)

            cache[node] = max(left, right) + 1
            return cache[node]


        getLen(root, {})
        return self.maxDiam