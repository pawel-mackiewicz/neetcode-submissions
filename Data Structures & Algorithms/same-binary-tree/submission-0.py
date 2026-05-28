# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = []
        qStack = []
        
        def putToStack(node: TreeNode | None, stack: list) -> None: 
            if not node:
                stack.append(None)
                return

            stack.append(node.val)

            putToStack(node.left, stack)
            putToStack(node.right, stack)

        putToStack(p, pStack)
        putToStack(q, qStack)

        return pStack == qStack

        
            