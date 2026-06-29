class UnionFind:
    def __init__(self):
        self._parents = {}
        self._sizes = {}
        self._ranks = {}

        self.maxSize = 1

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
        r1 = self._ranks[p1]
        r2 = self._ranks[p2]
        
        if r1 < r2:
            self._parents[p2] = p1
            self._sizes[p1] = currSize
        elif r1 > r2:
            self._parents[p1] = p2
            self._sizes[p2] = currSize
        else:
            self._parents[p1] = p2
            self._sizes[p2] = currSize
            self._ranks[p2] += 1

        self.maxSize = max(self.maxSize, currSize)
    
    def add(self, num):
        if num in self._parents:
            return
        
        self._parents[num] = num
        self._sizes[num] = 1
        self._ranks[num] = 1

        if num-1 in self._parents:
            self._union(num, num-1)
        if num+1 in self._parents:
            self._union(num, num+1)
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        uf = UnionFind()

        for num in nums:
            uf.add(num)
        
        return uf.maxSize