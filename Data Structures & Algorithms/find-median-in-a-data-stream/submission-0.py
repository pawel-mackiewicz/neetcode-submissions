class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.low, num)

        if ( 
            len(self.low) > len(self.high) + 1 or 
            (len(self.high) > 0 and self.low[0] > self.high[0])
        ):
            val = heapq.heappop_max(self.low)
            heapq.heappush(self.high, val)
            
        if len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush_max(self.low, val)


    def findMedian(self) -> float:
        # check if odd
        if len(self.low) != len(self.high):
            return self.low[0]
        else:
            return (self.low[0] + self.high[0]) / 2
        
        