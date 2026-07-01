class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        affordableProjects = []
        minCapital = list(zip(capital, profits))

        heapq.heapify(minCapital)

        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                _, p = heapq.heappop(minCapital) 
                heapq.heappush_max(affordableProjects, p)
                    
            if not affordableProjects:
                break

            w += heapq.heappop_max(affordableProjects)

        return w