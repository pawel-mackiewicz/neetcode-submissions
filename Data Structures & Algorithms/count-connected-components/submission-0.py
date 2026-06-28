class UnionFind:
    def __init__(self, n: int):
        self._parents = [i for i in range(n)]
        self._scores = [0] * n
        self.componentsCounter = n

    def find(self, node: int):
        while node != self._parents[node]:
            self._parents[node] = self._parents[self._parents[node]]
            node = self._parents[node]
        return node

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 == p2:
            return
        
        s1 = self._scores[p1]
        s2 = self._scores[p2]

        if s1 > s2:
            self._parents[p2] = p1
        elif s1 < s2:
            self._parents[p1] = p2
        else:
            self._parents[p1] = p2
            self._scores[p2] += 1

        self.componentsCounter -= 1
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        uf = UnionFind(n)

        for edge in edges:
            e1 = edge[0]
            e2 = edge[1]

            uf.union(e1,e2)
        
        return uf.componentsCounter

