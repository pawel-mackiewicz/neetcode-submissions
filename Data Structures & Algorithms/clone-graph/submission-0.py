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
        visited = set()

        # take current, take neighbors
        # create new node for each neighbor
        # append to current.neighbors
        # repeat for all neighbors

        def dfs(current: Node):
            if current in visited:
                return
            visited.add(current)
            if current in clones:
                clone = clones[current]
            else:
                clone = Node(current.val)
                clones[current] = clone

            for n in current.neighbors:
                if n in clones:
                    new = clones[n]
                else:
                    new = Node(n.val)
                    clones[n] = new
                clone.neighbors.append(new)
                dfs(n)
        dfs(node)
        return clones[node]