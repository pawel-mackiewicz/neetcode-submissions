class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        affordableProjects = []
        minCapital = [(c, p) for c,p in zip(capital, profits)]

        heapq.heapify(minCapital)

        for i in range(k):
            if minCapital:
                c, p = minCapital[0]
                while c <= w:
                    heapq.heappush_max(affordableProjects, p)
                    heapq.heappop(minCapital)
                    
                    if not minCapital:
                        break

                    c, p = minCapital[0]

            if affordableProjects:
                w += heapq.heappop_max(affordableProjects)
            else:
                break

        return w