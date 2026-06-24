class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
    
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n

    def union(self, m, n) -> bool:
        p = self.find(m)
        q = self.find(n)

        if p == q:
            return False

        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[p] < self.rank[q]:
            self.par[p] = q
        else:
            self.par[q] = p
            self.rank[p] += 1
        return True
 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for m,n in edges:
            if not uf.union(m,n):
                return [m,n]
        raise Exception("There is no edge to remove!")