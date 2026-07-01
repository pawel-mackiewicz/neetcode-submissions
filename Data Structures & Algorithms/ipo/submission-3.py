class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        affordableProjects = []
        minCapital = [(c, p) for c,p in zip(capital, profits)]

        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = minCapital[0]
                heapq.heappush_max(affordableProjects, p)
                heapq.heappop(minCapital)
                    
            if not affordableProjects:
                break

            w += heapq.heappop_max(affordableProjects)

        return w