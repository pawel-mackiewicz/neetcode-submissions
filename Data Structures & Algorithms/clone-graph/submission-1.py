"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # input node -> first val 1
        if not node:
            return None
        clones = {}

        def dfs(current: Node):
            if current in clones:
                return clones[current]

            clone = Node(current.val)
            clones[current] = clone

            for nei in current.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)