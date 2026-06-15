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

            cache[node] = max(getLen(node.left, cache),getLen(node.right, cache)) + 1
            return cache[node]


        def getDiam(node, cache):
            if not node:
                return

            self.maxDiam = max(self.maxDiam, getLen(node.left, cache) + getLen(node.right, cache))
            getDiam(node.left, cache)
            getDiam(node.right, cache)
            

        getDiam(root, {})
        return self.maxDiam