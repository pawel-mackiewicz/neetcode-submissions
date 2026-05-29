class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for i in range(len(nums)):
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, nums[i])
            else:
                heapq.heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else: 
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
            
            