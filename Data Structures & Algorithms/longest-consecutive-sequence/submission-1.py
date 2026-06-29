class UnionFind:
    def __init__(self):
        self._parents = {}
        self._sizes = {}

        self.maxSize = 0

    def _find(self, num):
        while num != self._parents[num]:
            self._parents[num] = self._parents[self._parents[num]]
            num = self._parents[num]

        return num

    def _union(self, num1, num2):
        p1 = self._find(num1)
        p2 = self._find(num2)

        if p1 == p2:
            return
        
        currSize = self._sizes[p1] + self._sizes[p2]
        
        if p1 < p2:
            self._parents[p2] = p1
            self._sizes[p1] = currSize
        else:
            self._parents[p1] = p2
            self._sizes[p2] = currSize

        self.maxSize = max(self.maxSize, currSize)
    
    def add(self, num):
        if num in self._parents:
            return
        
        self._parents[num] = num
        self._sizes[num] = 1

        if num-1 in self._parents:
            self._union(num, num-1)
        if num+1 in self._parents:
            self._union(num, num+1)
        
        self.maxSize = max(self.maxSize, self._sizes[num])
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num already in - skip
        # num-1 in - _union
        # num+1 in - _union

        uf = UnionFind()

        for num in nums:
            uf.add(num)
        
        return uf.maxSize